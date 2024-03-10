import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# Function to generate a fake conversation between two users
def generate_fake_conversation(chat_db, user1, user2, num_messages=10):
    messages = []
    message_dates = []
    start_date = datetime.now() - timedelta(days=30)  # Limit messages to last 30 days

    for _ in range(num_messages):
        message_from = user1 if random.random() < 0.5 else user2
        message_to = user2 if message_from == user1 else user1
        message_date = start_date + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))

        # Ensure messages are in chronological order
        if len(message_dates) > 0 and message_date < message_dates[-1]:
            message_date = message_dates[-1]  # Set message date to the latest date if out of order

        message_dates.append(message_date)
        message = fake.sentence()
        chat_db.add_message(message, message_from, message_to)
        messages.append({"message": message, "message_from": message_from, "message_to": message_to, "message_date": message_date})

    return messages

# # Generate fake conversations between users
# fake_conversations = []
# for i in range(len(users_dataset)):
#     for j in range(i+1, len(users_dataset)):
#         user1 = users_dataset[i]["user_id_email"]
#         user2 = users_dataset[j]["user_id_email"]
#         fake_messages = generate_fake_conversation(chatDb, user1, user2)
#         fake_conversations.append({"user1": user1, "user2": user2, "messages": fake_messages})

# # Print the fake conversations
# for conversation in fake_conversations:
#     print(f"Conversation between {conversation['user1']} and {conversation['user2']}:")
#     for message in conversation['messages']:
#         print(f"\t{message['message_date']}: {message['message']}")
