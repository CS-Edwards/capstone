
import glob
import os
import weaviate
import logging
import json
from weaviate.util import generate_uuid5
from client import create_client
from schema import create_schema

#TODO move to seperate file
#log error instead of print
#### FROM WEAVIATE DOCS ###
def check_batch_result(results: dict):
  """
  Check batch results for errors.

  Parameters
  ----------
  results : dict
      The Weaviate batch creation return value.
  """

  if results is not None:
    for result in results:
      if "result" in result and "errors" in result["result"]:
        if "error" in result["result"]["errors"]:
          print(result["result"])
######

#logging config
logging.basicConfig(filename='error_log.txt', level=logging.DEBUG)

client = create_client()
client.schema.delete_all() #remove any preexisting scheme and data 
print(client.schema.get()) #empty schema

schema = create_schema()
client.schema.create(schema)

print(client.schema.get()) 

client.batch.configure(
    batch_size=5,
    dynamic=True,
    callback=check_batch_result
)

# Retrieve prompt text files
directory = '../data/prompts/test_batch_1'
json_files = glob.glob(os.path.join(directory,'*.json'))



# populate client DB
with client.batch as batch:

    for file_path in json_files:
        try:
            with open(file_path,'r') as file:
                prompt_text = json.loads(file.read()) #must be a dict for data_object
            
            uuid_prompt = generate_uuid5(prompt_text,"Prompt")
            batch.add_data_object(
                data_object=prompt_text,
                class_name="Prompt",
                uuid=uuid_prompt
            )
            print(f"ADDED to DB: UUID {uuid_prompt} \n File:{file_path} \n Prompt:{prompt_text}")
        except FileNotFoundError as e:
            logging.error(f"File not found error: {e}")
        except Exception as e:
            logging.error(f"Error occured while processing file: {file_path}, Error: {e}")



##Query
