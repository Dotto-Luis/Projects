def get_prompt_template() -> str:
    """Prompt template for the banking document Q&A chain."""
    return (
        "Use the following context to answer the question. "
        "If the answer is not in the context, say you don't know.\n\n"
        "Question: {question}\n"
        "Context: {context}\n\n"
        "Answer:"
    )
