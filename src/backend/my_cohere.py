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
    self.chatDB = ChatDb()
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
    print(f"Messages list: {messages_list}")
    # Concatenate all messages into a single string
    
    chat_text = " ".join(messages_list)
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

    # # Add users
    # mongo.add_user("Nadia R", 'nadiar@gmail.com', 'password')
    # mongo.add_user("John Doe", 'johnd@gmail.com', 'password')

    # # Get user ObjectIds
    # user_nadia_id = mongo.get_id("nadiar@gmail.com")
    # user_john_id = mongo.get_id("johnd@gmail.com")

    # # Add fake messages between users to simulate a conversation
    # chat_db = ChatDb()
    # messages = [
    #     ("Hello, John. I'm excited to start our mentoring session today.", user_nadia_id,  user_john_id),
    #     ("Hi Nadia! I'm looking forward to it as well.",  user_john_id, user_nadia_id),
    #     ("I wanted to discuss a project I'm working on. Can I get your advice?", user_nadia_id,  user_john_id),
    #     ("Of course, I'd be happy to help. Tell me more about the project.",  user_john_id, user_nadia_id),
    #     ("It involves integrating a third-party API, and I'm stuck on the implementation details.", user_nadia_id,  user_john_id),
    #     ("Let's brainstorm together. One approach could be to decouple the API integration logic from the rest of your application using a service or adapter pattern.",  user_john_id, user_nadia_id),
    #     ("That makes sense. I'll look into implementing the service pattern for this feature. Thank you for the suggestion!", user_nadia_id,  user_john_id),
    #     ("You're welcome! If you have any more questions, feel free to ask.",  user_john_id, user_nadia_id)
    # ]

    # for message_text, sender, recipient in messages:
    #     chat_db.add_message(message_text, sender, recipient)

  
    # # # test summarize chat function
    # summary = my_cohere.summarize_chat(user_nadia_id, user_john_id)
    # print(f"Chat summary between {user_nadia_id} and {user_john_id}: {summary}")

      # Get all user profiles
    user_profiles = mongo.get_profiles("mentor")

    # Select a random user_id from user_profiles
    random_user_id = random.choice(user_profiles)
    random_user_id2 = random.choice(user_profiles)

    # test create suggested text function
    # ???

    # test user matching function
    print(mongo.get_preferences(random_user_id, "mentor"))
    user_type = "mentor"
    matches = my_cohere.user_matching(random_user_id, user_type)
    print(f"Matches: {matches}")

