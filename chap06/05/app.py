import gradio as gr
from generate_mess import generate_chat_response

with gr.Blocks() as demo:
    state = gr.State({
        "pre_id": None
    })
    chatbot = gr.Chatbot(type="messages")
    with gr.Row():
        msg = gr.Textbox(show_label=False, scale=7)
        with gr.Column(scale=1):
            submit = gr.Button("送信")
            clear = gr.ClearButton([msg, chatbot], value="リセット")


    async def respond(state, message, chat_history):
        # 会話履歴にユーザーの発言を追加
        chat_history.append({"role": "user", "content": message})
        bot_message = generate_chat_response(state, message)
        # エージェントの出力を会話履歴に追加
        chat_history.append({"role": "assistant", "content": bot_message})

        return "", chat_history

    gr.on(
        triggers=[msg.submit, submit.click],
        fn=respond,
        inputs=[state, msg, chatbot],
        outputs=[msg, chatbot],
    )

if __name__ == "__main__":
    demo.launch()