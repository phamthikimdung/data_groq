from langchain_groq import ChatGroq
import os

os.environ["GROQ_API_KEY"] = "your_groq_api_key"
def load_llm(model_name):

    if model_name == "llama-3.1-70b-versatile":
        return ChatGroq(
                            model=model_name,
                             temperature=0.0,
                             groq_api_key= os.environ["GROQ_API_KEY"],
                             verbose= True
        )
    else:
        raise ValueError(
            "Unknown model."
        )