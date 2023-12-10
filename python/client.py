import weaviate
from config import WEAVIATE_API_KEY

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
  url="https://test-db-0-xdqr0ls0.weaviate.network",
  auth_client_secret=auth_config
)


print(client.schema.get())