# chatbot_logic.py (Updated for modern LangChain)

import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

# --- UPDATED IMPORTS ---
# ChatOpenAI is now in its own 'langchain_openai' package
from langchain_openai import ChatOpenAI 
# Prompts and other core components are now in 'langchain_core'
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# Load environment variables from .env file
load_dotenv()

class Chatbot:
    def __init__(self):
        # 1. Initialize the LLM (Language Model)
        # No change here, but it's now using the class from the new package
        self.llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

        # 2. Define the Prompt Template (This is crucial for "Prompt Engineering")
        # No change to the logic, but it uses the newly imported classes
        prompt_template = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You are a friendly and helpful customer support assistant for 'Gadget World'. "
                    "Your goal is to answer questions about products, orders, and returns. "
                    "If you don't know the answer, say 'I'm sorry, I don't have that information, but I can connect you to a human agent.'"
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}")
            ]
        )

        # 3. Set up Memory (To handle "Context")
        # No change here
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # 4. Create the Conversation Chain
        # The LLMChain import and logic remains the same for this simple use case
        self.conversation_chain = LLMChain(
            llm=self.llm,
            prompt=prompt_template,
            verbose=True,
            memory=self.memory
        )

    def get_response(self, user_input: str) -> str:
        """
        Processes user input and returns the chatbot's response.
        """
        # The .invoke() method is the new standard, but .predict() still works for LLMChain
        # We'll keep .predict() for now as it's simpler for this chain type.
        response = self.conversation_chain.predict(question=user_input)
        return response

# You can create a single instance to be used by the API
chatbot_instance = Chatbot()