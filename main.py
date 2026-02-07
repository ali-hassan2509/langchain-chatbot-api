from fastapi import FastAPI
from pydantic import BaseModel

# Import the chatbot instance from our logic file
from chatbot_logic import chatbot_instance

# Initialize the FastAPI app
app = FastAPI(
    title="AI Chatbot API",
    description="An API for interacting with our AI Chatbot",
    version="1.0.0"
)

# Define the data model for the request body
# This ensures that any request to our endpoint has a 'message' field
class ChatRequest(BaseModel):
    message: str

# Define the data model for the response
class ChatResponse(BaseModel):
    reply: str

# Create the API endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    """
    Endpoint to receive a user message and return the chatbot's reply.
    """
    # Get the response from our chatbot logic
    response_text = chatbot_instance.get_response(request.message)
    
    # Return the response in the specified format
    return ChatResponse(reply=response_text)

# A simple root endpoint to check if the server is running
@app.get("/")
def read_root():
    return {"status": "AI Chatbot API is running."}