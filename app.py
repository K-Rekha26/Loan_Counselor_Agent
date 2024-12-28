from flask import Flask, request, jsonify
from flask_cors import CORS

# LoanCounselorAgent class
class LoanCounselorAgent:
    def handle_message(self, message):
        message = message.lower()
        if "eligibility" in message:
            return {"response": "To be eligible for a loan, you need a stable income, good credit score, and required documents."}
        elif "loan amount" in message or "how much loan" in message:
            return {"response": "The loan amount depends on your income, credit score, and other factors. Provide details for a personalized estimate."}
        elif "documents" in message:
            return {"response": "Common documents include ID proof, address proof, income proof, and bank statements."}
        elif "loan process" in message:
            return {"response": "The loan process involves application submission, verification, and approval. Need help with any step?"}
        else:
            return {"response": "I'm here to help with loan-related queries. Could you clarify your question?"}

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get("message", "")
        print(f"Received message: {message}")  # Log incoming message

        agent = LoanCounselorAgent()
        response = agent.handle_message(message)

        print(f"Sending response: {response}")  # Log outgoing response
        return jsonify(response)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# Run the server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
