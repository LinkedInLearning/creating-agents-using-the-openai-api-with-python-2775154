from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5-mini",
    tools=[{"type": "web_search"
        ,"search_context_size": "low"}],
    #instructions="回答は日本語でお願いします",
    input="何か楽しいのニュースはないかい?"
)

print(response.output_text)

# ログにWebからサーチしたことが記録される