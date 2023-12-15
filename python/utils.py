import os
import glob
import json

#
# Convert .txt to .json dict files
#



directory = '../data/prompts/test_batch_1'
txt_files = glob.glob(os.path.join(directory,'*.txt'))

for file_path in txt_files:
        try:
            with open(file_path,'r') as file:
                prompt_text = file.read()

            
        except FileNotFoundError as e:
             print(f'ERROR: {e}')
        
        prompt_dict = {
                "taskPrompt": prompt_text
            }

        output_file = os.path.join(directory,f"dict_out_{os.path.basename(file_path)}.json")

        with open(output_file, 'w',encoding='utf-8') as dictFile:
                dictFile.write(json.dumps(prompt_dict))