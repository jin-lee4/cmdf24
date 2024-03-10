# pip install stream-chat
from stream_chat import StreamChat

# instantiate your stream client using the API key and secret
# the secret is only used server side and gives you full access to the API
server_client = StreamChat(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
token = server_client.create_token("john")

server_client.upsert_user({"id": user_id, "role": "admin", "mycustomfield": "123"})
