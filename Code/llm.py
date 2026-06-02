import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chat_models import BaseChatModel

load_dotenv()

def get_llm(model_name:str, temperature: float = 0.2) -> BaseChatModel:
    return ChatGroq(
        api_key=os.getenv('GROQ_API_KEY'),
        model=model_name,
        temperature=temperature
    )