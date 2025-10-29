import gradio as gr

def greet(name):
    return "こんにちは、" + name + "さん"

# Blocksの作成
with gr.Blocks() as demo:
    # UI
    name = gr.Textbox(label="名前")
    output = gr.Textbox(label="出力ボックス")
    # interactive=Trueにすることで、テキストを入力できるようになる
    # output = gr.Textbox(label="出力ボックス", interactive=True)
    greet_btn = gr.Button("あいさつ")

    # イベントハンドラー
    greet_btn.click(fn=greet, inputs=name, outputs=output)

# 起動
demo.launch()