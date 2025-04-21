def get_prompt_template():
    return (
        "Usá el siguiente contexto para responder la pregunta.\n\n"
        "Pregunta: {question}\n"
        "Contexto: {context}\n\n"
        "Respuesta:"
    )
