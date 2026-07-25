from langchain_google_genai import ChatGoogleGenerativeAI

from config import GOOGLE_API_KEY
from src.prompts.template import prompt
from src.memory import memory


llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)


chain = prompt | llm



def ask_llm(question: str, context: str) -> str:

    response = chain.invoke(
        {
            "question": question,
            "context": context,
            "history": memory.messages
        }
    )


    memory.add_message(
        {
            "role": "user",
            "content": question
        }
    )


    memory.add_message(
        {
            "role": "assistant",
            "content": response.content
        }
    )


    return response.content