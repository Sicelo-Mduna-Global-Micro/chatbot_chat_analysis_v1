import requests
import json

# Define the endpoint and authentication details
endpoint = "https://flowgear-chatbot-phase1.eastus.inference.ml.azure.com/score"
api_key = "a8GozXrP5LD8mbBN2hBkJ2uHR19kHzjw"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Function to send a prompt to the chatbot
def get_response(prompt):
    data = {"prompt": prompt}
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    response = get_response(user_prompt)
    print("Chatbot response:", response)