import base64
from openai import OpenAI
client = OpenAI()

with open("invoice.pdf", "rb") as f:
    data = f.read()

base64_string = base64.b64encode(data).decode("utf-8")

response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "filename": "invoice.pdf",
                    "file_data": f"data:application/pdf;base64,{base64_string}",
                },
                {
                    "type": "input_text",
                    "text": "交通費は全部でいくらですか？",
                },
            ],
        },
    ]
)

print(response.output_text)