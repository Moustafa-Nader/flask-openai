import os

from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, request, jsonify

load_dotenv()  

app = Flask(__name__)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    chat_completion = client.chat.completions.create(
        messages=[
        {"role": "system", "content": "you are a helpful assistant"},
        {"role": "user", "content": user_message},
    ],
        model="gpt-3.5-turbo",
    )

    assistant_reply = chat_completion.choices[0].message.content
    
    return jsonify({"Reply": assistant_reply})


if __name__ == '__main__':
    app.run(debug=True)
