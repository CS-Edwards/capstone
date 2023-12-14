import weaviate
from config import WEAVIATE_API_KEY

def create_client():
  '''
  Creates a Weaviate client (v3.25.3) with WCS endpoint, out-of-the-box configuration.

  This function initializes a Weaviate client using WCS endpoint url and authentication.

  Returns:
      weaviate.Client: An instance of the Weaviate client.
  '''

  auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

  client = weaviate.Client(
    url="https://test-db-0-xdqr0ls0.weaviate.network",
    auth_client_secret=auth_config
  )


  print(client.schema.get()) #empty schema
  return client

