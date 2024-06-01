import os
from flask import Flask, request, jsonify, render_template

from openai import OpenAI

# Initialize the Flask app
app = Flask(__name__)

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("message")
        if user_input:
            # Send the user input to the API and stream the response
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input},
                ],
                stream=True,
            )

            # Extract the response from the stream
            reply = ""
            for chunk in stream:
                reply += chunk.choices[0].delta.content or ""

            return jsonify({"reply": reply})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
