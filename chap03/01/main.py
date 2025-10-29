from openai import OpenAI
client = OpenAI()

pre_id = None
def generate_response(user_input=""):
    global pre_id
    response = client.responses.create(
        model="gpt-5-mini",
        input=user_input,
        previous_response_id=pre_id,
        # previous_response_id = response.last_response_id if response else None
        # AttributeError: 'Response' object has no attribute 'last_response_id'
    )
    pre_id = response.id
    print("ボット: " + response.output_text.replace("\n", ""))
    print()

def main():
    while True:
        print("\n----------------------------------------\n")
        print(" こんにちは AI-CHATBOT です\n")
        print("選択してください\n")
        print("1 -> チャット開始")
        print("2 -> 終了")
        choice = input("1か2を押してください: ")
        if choice == "1":
            start_chat()
        elif choice == "2":
            exit()
        else:
            print("正しく入力してください")

def start_chat():
    print("チャットを終わるには End と入力してください")
    print("\n      新規チャット       ")
    print("---------------------")

    while True:
        user_input = input("あなた: ")

        if user_input.lower() == "end":
            break
        else:
            generate_response(user_input)

if __name__ == "__main__":
    main()