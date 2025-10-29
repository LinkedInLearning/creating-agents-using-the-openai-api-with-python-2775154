from openai import OpenAI

client = OpenAI()

MODEL_ENGINE = "gpt-5-mini"
ROLE_SYSTEM = {"role": "system", "content":"あなたは有能なエージェントです。いつでも適切な助言を与えてくれます。"} 

pre_id = None


def generate_chat_response(user_input=""):
    global pre_id
    response = client.responses.create(
        model=MODEL_ENGINE,
        input = user_input,
        previous_response_id = pre_id
    )
    pre_id = response.id
    return response.output_text
