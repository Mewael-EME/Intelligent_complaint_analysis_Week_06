# src/prompt_template.py

def build_prompt(question: str, context_chunks: list):
    context = "\n---\n".join(context_chunks)
    prompt = (
        "You are a financial analyst assistant for CrediTrust. "
        "Your task is to answer questions about customer complaints. "
        "Use the following retrieved complaint excerpts to formulate your answer. "
        "If the context doesn't contain the answer, say you don't have enough information.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n"
        f"Answer:"
    )
    return prompt
 
