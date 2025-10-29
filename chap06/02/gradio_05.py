import gradio as gr

# イベントリスナーにより呼び出される関数
def welcome(name):
    return f"ようこそ、学びの世界に {name}さん"

# Blocksの作成
with gr.Blocks() as demo:
    # コンポーネント
    gr.Markdown(
    """
    # こんにちは、Gradioへようこそ！
    ### 文字を入力しながら、表示の変化を楽しんでください。
    """)
    inp = gr.Textbox(placeholder="お名前をどうぞ")
    out = gr.Textbox()

    # イベントリスナー
    inp.change(welcome, inp, out)


# 起動
demo.launch()
