from dotenv import load_dotenv
import os
load_dotenv()

from langchain_groq import ChatGroq

def get_llm():
    llm = ChatGroq(model='openai/gpt-oss-120b')
    return llm