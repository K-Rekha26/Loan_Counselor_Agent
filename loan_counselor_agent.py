class LoanCounselorAgent:
    def handle_message(self, message):
         message = message.lower()
         if "interest" in message:
            return {"response": "I can help you with loan interest rates. What type of loan are you interested in?"}
         elif "eligibility" in message:
            return {"response": "I can assist you with loan eligibility. Please provide your details."}
         elif "type of loan" in message:
            return {"response": "We offer personal loans, home loans, and car loans. Which one are you interested in?"}
         elif "apply" in message:
            return {"response": "To apply for a loan, I'll need some details. Can you provide your personal information?"}
         else:
            return {"response": f"Received: {message}"}
