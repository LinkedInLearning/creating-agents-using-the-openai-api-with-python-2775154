import gradio as gr
from agents import Runner, InputGuardrailTripwireTriggered
from my_agents import triage_agent, func_call_agent, web_search_agent, doc_search_agent


with gr.Blocks() as demo:
    state = gr.State({
        "pre_id": None,
        "current_agent_name": triage_agent.name
    })
    # UI を定義
    chatbot = gr.Chatbot(type="messages")
    with gr.Row():
        msg = gr.Textbox(show_label=False, scale=7)
        with gr.Column(scale=1):
            submit = gr.Button("送信")
            clear = gr.ClearButton([msg, chatbot], value="リセット")

    async def respond(state, message, chat_history):

        """メッセージ送信時の処理"""
        # 会話履歴にユーザーの発言を追加
        chat_history.append({"role": "user", "content": message})
        match state["current_agent_name"]:
            case func_call_agent.name:
                current_agent = func_call_agent
            case web_search_agent.name:
                current_agent = web_search_agent
            case doc_search_agent.name:
                current_agent = doc_search_agent
            case _:
                current_agent = triage_agent
        try:
            # エージェントに会話履歴を送信
            response = await Runner.run(
                current_agent, message, previous_response_id=state["pre_id"]
            )
            state["pre_id"] = response.last_response_id
            state["current_agent_name"] = response.last_agent.name 
            bot_message = response.final_output
            # エージェントの出力を会話履歴に追加
            chat_history.append({"role": "assistant", "content": bot_message})
            # Gradui UI に会話履歴を返す
            return "", chat_history
        except InputGuardrailTripwireTriggered as e:
            # ガードレールがトリガーされた場合の処理
            chat_history.append(
                {
                    "role": "assistant",
                    "content": f"不適切な入力が見つかりました。お返事できません。",
                }
            )
            return "", chat_history

    # Gradio UI にコールバックを設定
    gr.on(
        triggers=[msg.submit, submit.click],
        fn=respond,
        inputs=[state, msg, chatbot],
        outputs=[msg, chatbot],
    )

if __name__ == "__main__":
    demo.launch()