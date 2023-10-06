from flask import Flask, request, jsonify
import subprocess


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def interact_with_main_program():
    try:
        # Get the input text from the request
        input_text = request.json['input_text']

        # Run the main program and capture its output
        command = f'../qwen.cpp/build/bin/main -p "{input_text}"'
        output = subprocess.check_output(command, shell=True, text=True)

        # Return the output as a JSON response
        return jsonify({'response': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
