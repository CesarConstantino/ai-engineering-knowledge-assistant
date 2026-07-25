from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from src.llm import ask_llm
from src.retriever import search_documents


class GraphState(TypedDict):
    question: str
    context: str
    answer: str



def retrieve(state: GraphState):

    context = search_documents(
        state["question"]
    )

    return {
        "context": context
    }



def chatbot(state: GraphState):

    answer = ask_llm(
        state["question"],
        state["context"]
    )

    return {
        "answer": answer
    }



builder = StateGraph(GraphState)


builder.add_node(
    "retrieve",
    retrieve
)


builder.add_node(
    "chatbot",
    chatbot
)


builder.add_edge(
    START,
    "retrieve"
)


builder.add_edge(
    "retrieve",
    "chatbot"
)


builder.add_edge(
    "chatbot",
    END
)


graph = builder.compile()