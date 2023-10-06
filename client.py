import requests
import re

# Function to read source text from file
def extract_and_execute(text):
    # Use a regex pattern to extract code between ` ```python` or just ` ``` ` and the ending ` ``` `
    pattern = r'```(?:python)?(.*?)```'
    code_snippets = re.findall(pattern, text, re.DOTALL)
    
    if not code_snippets:
        # If no code blocks are found, consider the entire text as code
        code_snippets = [text.strip()]
    
    for snippet in code_snippets:
        # Strip to remove any leading/trailing whitespace or newline
        code = snippet.strip()
        print(f"Executing code:\n{code}\n")
        exec(code)

# Define the API endpoint URL
api_url = 'http://127.0.0.1:5000/api'

# Input text to send to the server
input_text = """g
               generate me a code that prints hi on the screen
               The name of my file is (all_stocks_5yr.csv) Here the format of my csv, 
               date,open,high,low,close,volume,Name
               2013-02-08,15.07,15.12,14.63,14.75,8407500,AAL
               2013-02-11,14.89,15.01,14.26,14.46,8882000,AAL
               make me a python code that calculate what the opening price the Febraruy 8th 2013 using pandas
               """

# Create a JSON payload
payload = {'input_text': input_text}

# Send a POST request to the API
response = requests.post(api_url, json=payload)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    data = response.json()
    code_to_execute = data['response']
    
    # Execute the code received from the API
    extract_and_execute(code_to_execute)
else:
    print('Error:', response.text)
