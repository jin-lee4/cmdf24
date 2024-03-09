import cohere

class MyCohere:
  """
  A class of functions using the Cohere API
  """
  def __init__(self):
    self.co = cohere.Client('p1uXN7nDABSGatQQVL8aMeEn40xUoDK2pGbuCa1q')

  def summarize_chat(self, text: str, date_range):
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
    response = self.co.summarize(text=sample_text, length="medium", format="bullets", extractiveness="auto" )
    # Extract the summarized text from the response tuple (id, summarised text, meta)
    summary_text = response[1]
    return summary_text


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
  summary_text = my_cohere.summarize_chat(sample_text, date_range="last 7 days")
  print(summary_text)


