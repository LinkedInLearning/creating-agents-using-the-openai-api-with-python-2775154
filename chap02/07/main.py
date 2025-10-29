from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "user", 
        "content": "[1,2],[3,4],[5,6]' という形式の文字列として表される行列を受け取り、同じ形式で転置を出力するbashスクリプトを作成してください。"
    }    
]
response = client.responses.create(
    model="gpt-5-mini",
    reasoning={"effort": "medium"}, #high,medium,low,minimal
    input=messages
)
print(response.output_text)