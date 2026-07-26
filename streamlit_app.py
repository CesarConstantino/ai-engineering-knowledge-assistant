import asyncio

import streamlit as st


# Crear event loop para Streamlit
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


from src.graph import graph


st.set_page_config(
    page_title="AI Engineering Knowledge Assistant",
    page_icon="🤖"
)


st.title("🤖 AI Engineering Knowledge Assistant")

st.write(
    """
    Asistente inteligente basado en RAG
    utilizando LangGraph, FAISS y Google Gemini.
    """
)


question = st.text_input(
    "Escribe tu pregunta:"
)


if st.button("Preguntar"):

    if question:

        with st.spinner("Consultando conocimiento..."):

            try:

                result = graph.invoke(
                    {
                        "question": question,
                        "context": "",
                        "answer": ""
                    }
                )


                st.subheader("Respuesta")

                st.write(
                    result.get("answer")
                )


            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

    else:

        st.warning(
            "Escribe una pregunta."
        )