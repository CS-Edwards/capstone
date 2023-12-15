

def create_schema():
    '''
    basic schema for database, containing Prompt class, for text prompts 
    '''

    schema = {
        "classes":[{
            "class": "Prompt",
            "description": "a text prompt for data science task",
            "properties":[
                {
                    "dataType":[
                        "text"
                    ],
                    "description": "text prompt",
                    "name":"taskPrompt"

                }
            ]
        }]
    }

    return schema
