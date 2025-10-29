import gradio as gr

with gr.Blocks() as demo:
    with gr.Column(scale=1, min_width=300):
        gr.Textbox(label="メールアドレス", type="email") 
        gr.Textbox(label="電話番号")
    # gr.Button("登録", variant="primary")  # secondary
    gr.Button("登録", variant="secondary")  # secondary

demo.launch()