import gradio as gr
from agents import Agent, Runner

last_id = None
with gr.Blocks() as demo:
    # UI を定義
    chatbot = gr.Chatbot(type="messages")
    with gr.Row():
        msg = gr.Textbox(show_label=False, scale=7)
        with gr.Column(scale=1):
            submit = gr.Button("送信")
            clear = gr.ClearButton([msg, chatbot], value="リセット")

    agent = Agent(
        name="Assistant",
        model="gpt-5-mini", 
        instructions="あなたは役に立つAIアシスタントです。"
    )

    async def respond(message, chat_history):
        global last_id
        """メッセージ送信時の処理"""
        # 会話履歴にユーザーの発言を追加
        chat_history.append({"role": "user", "content": message})

        # エージェントに会話履歴を送信
        response = await Runner.run(
            agent, message, 
            previous_response_id = last_id,
        )
        bot_message = response.final_output
        # エージェントの出力を会話履歴に追加
        chat_history.append({"role": "assistant", "content": bot_message})
        last_id = response.last_response_id 

        # Gradio UI に会話履歴を返す
        return "", chat_history

    # Gradio UI にコールバックを設定
    gr.on(
        triggers=[msg.submit, submit.click],
        fn=respond,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot],
    )

if __name__ == "__main__":
    demo.launch(share=True, debug=True)