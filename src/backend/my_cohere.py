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
    """
    # Get the preferences of the user
    user_preferences = self.userDB.get_preferences(user_id)
    
    # Initialize an empty list to store the matches
    matches = []
    
    # If the user is a mentor
    if user_type == "mentor":
        # Get list of mentees
        mentees_list = self.userDB.get_all_mentees()
        for mentee in mentees_list:
            # Get the preferences of the mentee
            mentee_preferences = self.userDB.get_preferences(mentee["_id"])
            # add the mentee id and their preferences to a dictionary
            user_dict = {"id": mentee["_id"], "preferences": mentee_preferences}

    
    # If the user is a mentee
    elif user_type == "mentee":
        # Get all mentors
        mentors = self.userDB.get_all_mentors()
        # Iterate over all mentors
        for mentor in mentors:
            # Get the preferences of the mentor
            mentor_preferences = self.userDB.get_preferences(mentor["_id"])
            # add the mentor id and their preferences to a dictionary
            user_dict = {"id": mentor["_id"], "preferences": mentor_preferences}

    prompt = f"Based on the preferences of the user {user_preferences}, please find a couple of matches from {user_dict}. Stricly return a list of user ids only."
    matches = self.co.generate(prompt=prompt)
    
    # Return the list of matches
    return matches
   
# TESTING
if __name__ == "__main__":
  my_cohere = MyCohere()

  sample_text=(
  "Ice cream is a sweetened frozen food typically eaten as a snack or dessert. "
  "It may be made from milk or cream and is flavoured with a sweetener, "
  "either sugar or an alternative, and a spice, such as cocoa or vanilla, "
  "or with fruit such as strawberries or peaches. "
  "It can also be made by whisking a flavored cream base and liquid nitrogen together. "
  "Food coloring is sometimes added, in addition to stabilizers. "
  "The mixture is cooled below the freezing point of water and stirred to incorporate air spaces "
  "and to prevent detectable ice crystals from forming. The result is a smooth, "
  "semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). "
  "It becomes more malleable as its temperature increases.\n\n"
  "The meaning of the name \"ice cream\" varies from one country to another. "
  "In some countries, such as the United States, \"ice cream\" applies only to a specific variety, "
  "and most governments regulate the commercial use of the various terms according to the "
  "relative quantities of the main ingredients, notably the amount of cream. "
  "Products that do not meet the criteria to be called ice cream are sometimes labelled "
  "\"frozen dairy dessert\" instead. In other countries, such as Italy and Argentina, "
  "one word is used fo\r all variants. Analogues made from dairy alternatives, "
  "such as goat's or sheep's milk, or milk substitutes "
  "(e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are "
  "lactose intolerant, allergic to dairy protein or vegan."
  )

  # test summarize chat function
  # summary_text = my_cohere.summarize_chat(sample_text, date_range="last 7 days")
  # print(summary_text)

  # # test create suggested text function
  # last_message = "I am Nadia, a final year computer science student and I am interested in AI. I would love to chat with you as a mentee."
  # suggested_response = my_cohere.create_suggested_text(last_message, sender="mentor", recipient="mentee", sender_name="John", recipient_name="Nadia")
  # print(suggested_response)


