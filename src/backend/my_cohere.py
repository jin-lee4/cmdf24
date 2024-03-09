import cohere
import os
from dotenv import load_dotenv

load_dotenv(".env")

class MyCohere:
  """
  A class of functions using the Cohere API
  """
  def __init__(self):
    self.co = cohere.Client(os.environ.get('COHERE_KEY'))

  def summarize_chat(self, chat_text: str, date_range) -> str:
    """
    Summarize chat messages
    Args:
    - text (str): chat messages
    - date_range (str): date range for the chat messages
    Returns:
    - summary_text (str): summarized text in bullet point form
    """
    # TODO: Extract text from database based on specified date range
    ## CODE HERE ##

    # Call the summarize method from the cohere client
    response = self.co.summarize(text=chat_text, length="medium", format="bullets", extractiveness="auto" )
    # Extract the summarized text from the response tuple (id, summarised text, meta)
    summary_text = response[1]
    return summary_text

  def create_suggested_text(self, last_message: str, sender: str, recipient: str, sender_name: str, recipient_name: str) -> str:
    """
    Create a suggested response based on the last message

    Args:
    - last_message (str): the last message in the chat
    - sender (str): the potential sender of the suggested text (either 'mentor' or 'mentee')
    - recipient (str): the potential sender of the suggested text (either 'mentor' or 'mentee')
    
    Returns:
    - suggested_response (str): the suggested response based on the last message
    """
    # Construct the prompt using the last message, sender, and recipient information
    my_prompt = f"Based on the last message from a {recipient} named {recipient_name}, please suggest a response: {last_message} in the perspective of a {sender} called {sender_name}."
    
    # Generate a response based on the prompt
    generate_output = self.co.generate(prompt=my_prompt)
    
    # Access the first generated response and extract the text
    suggested_response = generate_output[0].text
    
    # Return the suggested response
    return suggested_response


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

  # test create suggested text function
  last_message = "I am Nadia, a final year computer science student and I am interested in AI. I would love to chat with you as a mentee."
  suggested_response = my_cohere.create_suggested_text(last_message, sender="mentor", recipient="mentee", sender_name="John", recipient_name="Nadia")
  print(suggested_response)


