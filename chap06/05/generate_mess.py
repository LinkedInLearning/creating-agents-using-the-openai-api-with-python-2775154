from openai import OpenAI

client = OpenAI()

MODEL_ENGINE = "gpt-5-mini"
ROLE_SYSTEM = {"role": "system", "content":"あなたは有能なエージェントです。いつでも適切な助言を与えてくれます。"} 


def generate_chat_response(state, user_input=""):
    response = client.responses.create(
        model=MODEL_ENGINE,
        input = user_input,
        previous_response_id = state["pre_id"]
    )
    state["pre_id"] = response.id
    return response.output_text
