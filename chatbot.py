from flask import Flask, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data if necessary
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define chat pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"sorry (.*)",
        ["No need to apologize, it's okay.",]
    ],
    [
        r"quit",
        ["Bye, take care. Have a great day!",]
    ],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Initialize Flask app
app = Flask(__name__)

# Define route for chat
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = chatbot.respond(user_message)
    return jsonify({"message": response})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
