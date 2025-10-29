from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    #model="gpt-5",
    model="gpt-5-mini",
    #model="gpt-5-nano",
    instructions="小さい子供にわかるように答えてください",
    input="夏らしい俳句を作ってください",
)

# print(response.output_text) 

'''
# Chat Completion API
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {   
            "role": "developer", 
            "content": "あなたは有能なアシスタントです。"
        },
        {
            "role": "user",
            "content": "プログラミングにおける再帰について俳句を作ってください"
        }
    ]
)
print(completion.choices[0].message)
'''