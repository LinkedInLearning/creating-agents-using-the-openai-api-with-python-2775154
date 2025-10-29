from openai import OpenAI
client = OpenAI()

# file = client.files.create(
#     file=open("menu.pdf", "rb"),
#     purpose="user_data"
# )

response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": "file-ELpLxeH72fYBfgReENfrjG",
                },
                {
                    "type": "input_text",
                    "text": "豆腐料理はいくつありますか？",
                },
            ]
        }
    ]
)

print(response.output_text)