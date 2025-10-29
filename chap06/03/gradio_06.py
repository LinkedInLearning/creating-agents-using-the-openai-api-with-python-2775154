import gradio as gr
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'height': np.random.randint(50, 70, 25),
    'weight': np.random.randint(120, 320, 25),
})

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# データ解析ダッシュボード")
        gr.Button("更新", scale=0 ,variant='primary') 

    with gr.Row(equal_height=True):
        with gr.Column(scale=1, min_width=250):
            gr.Markdown("## 設定")
            with gr.Group():
                gr.Slider(label="データ範囲", value=25, minimum=1, maximum=50, step=1, interactive=True)
                gr.Dropdown(label="可視化タイプ", choices=["線グラフ", "棒グラフ"], value="線グラフ", interactive=True)
                gr.Radio(choices=["値あり", "値なし"], label="凡例表示", value="値あり", interactive=True)
                gr.Checkbox(label="グリッド表示", value=True, interactive=True)
        with gr.Column(scale=2):
            gr.ScatterPlot(df, x="weight", y="height", height=300, width=500, label="weight vs height")

    with gr.Row():
        gr.Markdown("copyright 2025")
demo.launch()