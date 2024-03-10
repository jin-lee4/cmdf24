import random
from bson import ObjectId
import cohere
import os
from dotenv import load_dotenv
from user_db_functions import *
from chat_db_functions import *

load_dotenv(".env")

class MyCohere:
  """
  A class of functions using the Cohere API
  """
  def __init__(self):
    self.co = cohere.Client(os.environ.get('COHERE_KEY'))
    self.chatDB = ChatDB()
    self.userDB = UserDB()

  def summarize_chat(self, sender_id: ObjectId, recipient_id: ObjectId, date_from: datetime=None, date_to: datetime=None) -> str:
    """
    Summarize chat messages
    Args:
    - text (str): chat messages
    - date_range (str): date range for the chat messages
    Returns:
    - summary_text (str): summarized text in bullet point form
    """
    # Extract text from database based on specified date range
    messages_list = self.chatDB.get_messages(sender_id, recipient_id, from_date=date_from, to_date=date_to)
    # Concatenate all messages into a single string
    chat_text = " ".join([message["message"] for message in messages_list])
    # Call the summarize method from the cohere client
    response = self.co.summarize(text=chat_text, length="medium", format="bullets", extractiveness="auto" )
    # Extract the summarized text from the response tuple (id, summarised text, meta)
    summary_text = response[1]
    return summary_text

  def create_suggested_text(self, sender_id: ObjectId, recipient_id: ObjectId) -> str:
    """
    Create a suggested response based on the last message

    Args:
    - sender_id (str): the id of the potential sender of the suggested text
    - recipient_id (str): the id of the potential recipient of the suggested text
    
    Returns:
    - suggested_response (str): the suggested response based on the last message
    """
    # get name of sender and recipient
    sender_name = self.userDB.get_name(sender_id)
    recipient_name = self.userDB.get_name(recipient_id)

    # Construct the prompt using the last message, sender, and recipient information
    my_prompt = f"Based on the last message (sentence) from {recipient_name}, please suggest a response in the perspective of {sender_name}. Only respond with the next sentence, nothing else."
    
    # Generate a response based on the prompt
    generate_output = self.co.generate(prompt=my_prompt)
    
    # Access the first generated response and extract the text
    suggested_response = generate_output[0].text
    
    # Return the suggested response
    return suggested_response


  def user_matching(self, user_id: ObjectId, user_type: str) -> list:
    """
    Match a user with a mentor or mentee based on their user type

    Args:
    - user_id (str): the id of the user
    - user_type (str): the type of the user (mentor or mentee)
    
    Returns:
    - matches (list): a list of matches (user_id) based on the user type & preferences
                      mentee's interests match with mentor's specialties
    """
    # Get the preferences of the user
    user_preferences = self.userDB.get_preferences(user_id, user_type)
    
    # Initialize an empty list to store the matches
    matches = []
    users_list = []
    
    # If the user is a mentor
    if user_type == "mentor":
        # Get list of mentees
        mentees_list = self.userDB.get_profiles("mentee")
        for mentee in mentees_list:
            # Get the interest of the mentee string
            mentee_preferences = self.userDB.get_preferences(mentee, "mentee")
            # add the mentee id and their interests to a list of users in tuple form (mentee_id, mentee_interests)
            users_list.append((mentee, mentee_preferences))

    
    # If the user is a mentee
    elif user_type == "mentee":
        # Get list of all mentors
        mentors = self.userDB.get_profiles("mentor")
        # Iterate over all mentors
        for mentor in mentors:
            # Get the specialty of the mentor (string)
            mentor_preferences = self.userDB.get_preferences(mentor, "mentor")
            # add the mentor id and their specialties to a list of matches in tuple form (mentor_id, mentor_specialties)
            users_list.append((mentor, mentor_preferences))

    # prompt = f"Based on the preferences of the user {user_preferences}, please find a couple of matches 
    # from {users_list}. every tuple is (user_id, specialties/interest). Generate the response stricly in
    #   this format [user_id1, user_id2, user_id3, ...]. Don't include any other information or say anything"
    
    prompt = f"Based on the preferences of the user {user_preferences}, please find a couple of matches from "
    prompt += "[" + ", ".join([f'{user[0]}' for user in users_list]) + "]. "
    prompt += "Every tuple is (user_id, specialties/interest). "
    prompt += "Generate the response strictly in this format [user_id1, user_id2, user_id3, ...]. "
    prompt += "Don't include any other information or say anything."

    # Current limitations: cant take more than 4081 tokens in the prompt
    # matches = self.co.generate(prompt=prompt, max_tokens=10000, stream=True)
    results = self.co.generate(prompt=prompt)
    generated_response = results[0].text

    # Check if the generated response is a list but in string form
    if generated_response.startswith("[") and generated_response.endswith("]"):
        # Convert the string to a list
        matches = eval(generated_response)
    else:
        # Otherwise, assume the generated response is already a list
        matches = generated_response



    return matches
   
# TESTING
if __name__ == "__main__":
  my_cohere = MyCohere()
  mongo = UserDB()

  # # test summarize chat function
  # summary_text = my_cohere.summarize_chat(sample_text, date_range="last 7 days")
  # print(summary_text)

  # # test create suggested text function
  # last_message = "I am Nadia, a final year computer science student and I am interested in AI. I would love to chat with you as a mentee."
  # suggested_response = my_cohere.create_suggested_text(last_message, sender="mentor", recipient="mentee", sender_name="John", recipient_name="Nadia")
  # print(suggested_response)

  # test user matching function
  # Get all user profiles
  user_profiles = mongo.get_profiles("mentor")

  # Select a random user_id from user_profiles
  random_user_id = random.choice(user_profiles)
  # print(mongo.get_preferences(random_user_id, "mentor"))
  user_type = "mentor"
  matches = my_cohere.user_matching(random_user_id, user_type)
  print(f"Matches: {matches}")

