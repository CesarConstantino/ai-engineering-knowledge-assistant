from langchain_core.tools import tool


@tool
def current_user() -> str:
    """
    Devuelve información del usuario actual.
    """

    return (
        "El usuario se llama César Constantino. "
        "Está desarrollando un AI Engineering Knowledge Assistant "
        "y su especialidad es Prevención de Fraude con IA."
    )