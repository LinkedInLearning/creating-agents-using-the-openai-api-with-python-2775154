import gradio as gr

def greet(name):
    return "Hello " + name + "!"

# Interfaceの作成
demo = gr.Interface(
    fn=greet, 
    inputs="text", 
    outputs="text"
)

# 起動
demo.launch()