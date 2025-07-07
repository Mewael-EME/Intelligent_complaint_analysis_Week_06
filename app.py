import gradio as gr
from src.rag_pipeline import generate_answer

# Function to use in Gradio
def rag_chatbot(question):
    answer, sources = generate_answer(question)
    source_text = "\n\n".join([f"🔹 {chunk}" for chunk in sources])
    return answer.strip(), source_text.strip()

# Gradio UI layout
with gr.Blocks(title="CrediTrust Complaint Assistant") as demo:
    gr.Markdown("# 🤖 CrediTrust Internal Complaint Assistant")
    gr.Markdown("Ask a question to understand customer complaint trends.")

    with gr.Row():
        question_input = gr.Textbox(label="Enter your question", placeholder="e.g. Why are customers unhappy with BNPL?")
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")

    with gr.Row():
        answer_output = gr.Textbox(label="Answer", lines=5)
        source_output = gr.Textbox(label="Sources (Complaint Excerpts)", lines=10)

    # Button interactions
    submit_btn.click(fn=rag_chatbot, inputs=question_input, outputs=[answer_output, source_output])
    clear_btn.click(lambda: ("", ""), outputs=[answer_output, source_output])

# Launch the app
if __name__ == "__main__":
    demo.launch()
 
