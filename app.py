from flask import Flask, request, jsonify

app = Flask(__name__)

def process_message(message):
    """Process the user message and generate a response."""
    message = message.strip().lower()  # Normalize the message

    # Match specific queries first
    if "eligibility criteria" in message or "eligible" in message:
        return "To be eligible for a loan, you need a stable income, good credit score, and required documents."
    elif "how much loan" in message or "loan amount" in message:
        return "The loan amount depends on your income, credit score, and other factors. Provide details for a personalized estimate."
    elif "car loan" in message:
        return "Yes, you can apply for a car loan. Would you like details on eligibility or interest rates?"
    elif "how to take loan" in message or "loan process" in message:
        return "To apply for a loan, you'll need to provide your income proof, ID documents, and credit history. Contact your bank for further steps."
    elif "loan" in message:
        return "Sure, what loan-related question do you have?"
    elif "hello" in message or "hi" in message:
        return "Hello! How can I assist you with your loan-related queries?"
    elif "love" in message:
        return "I'm just a bot, but I appreciate the sentiment!"
    else:
        return "Could you clarify your question? I'm here to help with loan-related queries."

@app.route('/chat', methods=['POST'])
def chat():
    """Handle incoming chat requests."""
    message = request.json.get('message', "")
    response_text = process_message(message)
    response = {"response": response_text}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
    from flask import Flask, request, jsonify

app = Flask(__name__)

def process_message(message):
    """Process the user message and generate a response."""
    message = message.strip().lower()  # Normalize the message

    # Match specific queries first
    if "eligibility criteria" in message or "eligible" in message:
        return "To be eligible for a loan, you need a stable income, good credit score, and required documents."
    elif "how much loan" in message or "loan amount" in message:
        return "The loan amount depends on your income, credit score, and other factors. Provide details for a personalized estimate."
    elif "car loan" in message:
        return "Yes, you can apply for a car loan. Would you like details on eligibility or interest rates?"
    elif "how to take loan" in message or "loan process" in message:
        return "To apply for a loan, you'll need to provide your income proof, ID documents, and credit history. Contact your bank for further steps."
    elif "loan" in message:
        return "Sure, what loan-related question do you have?"
    elif "hello" in message or "hi" in message:
        return "Hello! How can I assist you with your loan-related queries?"
    elif "love" in message:
        return "I'm just a bot, but I appreciate the sentiment!"
    else:
        return "Could you clarify your question? I'm here to help with loan-related queries."

@app.route('/chat', methods=['POST'])
def chat():
    """Handle incoming chat requests."""
    message = request.json.get('message', "")
    response_text = process_message(message)
    response = {"response": response_text}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

