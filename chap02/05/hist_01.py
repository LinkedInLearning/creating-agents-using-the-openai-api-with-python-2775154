# 会話の履歴をコードで追加するサンプル
from openai import OpenAI

client = OpenAI()

history = [
    {
        "role": "user",
        "content": "何か面白い話をして"
    }
]

response = client.responses.create(
    model="gpt-5-mini",
    input=history,
    store=False # 会話履歴をサーバー側に保持させる設定 default: True
)

print(response.output_text)

# Add the response to the conversation
for el in response.output:
    if hasattr(el, 'role'):
        history += [{"role": el.role, "content": el.content}]

history.append({ "role": "user", "content": "別の面白い話をして" })

second_response = client.responses.create(
    model="gpt-5-mini",
    input=history,
    store=False # 会話履歴をサーバー側に保持させる設定 default: True
)

print(second_response.output_text)