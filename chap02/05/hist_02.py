from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    input="代表的な夏野菜をいくつか教えて",
    #store=True  # 会話履歴をサーバー側に保持させる設定 default: True
)
print(response.output_text)

second_response = client.responses.create(
    model="gpt-5-mini",
    previous_response_id=response.id,
    input=[{"role": "user", "content": "それらの栄養素を教えて"}],
)
print(second_response.output_text)