import gradio as gr

with gr.Blocks() as demo:
    with gr.Row(equal_height=True):
        name_first = gr.Textbox(label="姓", min_width=150)
        name_last = gr.Textbox(label="名", min_width=150)
    gr.Button("送信")
demo.launch()