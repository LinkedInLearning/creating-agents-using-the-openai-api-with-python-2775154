from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()   #上位フォルダにある.envファイルも読んでくれる
client = OpenAI()

MODEL_ENGINE = "gpt-5-mini"
ROLE_SYSTEM = {"role": "system", "content":"あなたは優秀な教授です"} 

pre_id = None

messages = []
messages.append(ROLE_SYSTEM)


def generate_chat_response(user_input=""):
    global pre_id
    messages.append({"role": "user", "content": user_input})
    response = client.responses.create(
        model=MODEL_ENGINE,
        input = user_input,
        previous_response_id = pre_id
    )
    pre_id = response.id
    message = {"role": "assistant", "content": response.output_text} 
    messages.append(message)
    return response.output_text
    # print("ボット: " + message.content.replace("\n", ""))