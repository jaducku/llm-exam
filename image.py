import os
import openai

os.environ["OPENAI_API_KEY"] = "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" # 환경변수에 OPENAI_API_KEY를 설정합니다.
openai.api_key = os.getenv("OPENAI_API_KEY")

def openai_llm(input_text, chat_history):

    if len(chat_history) == 0:
        chat_history.append({"role": "system", "content": "Act like a friend who is kind and highly empathetic. Respond to the user's input in a friendly and conversational manner in Korean"})

    chat_history.append({"role": "user", "content": input_text})

    completion = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                messages=chat_history)

    output = completion.choices[0].message.content

    chat_history.append({"role": "assistant", "content": output})

    print(chat_history)

    return output

def chat_with_user(user_message, chat_history):
    ai_message = openai_llm(user_message, chat_history)
    return ai_message

chat_history = []

while True:
    user_message = input("USER > ")
    if user_message.lower() == "quit":
        break
    ai_message = chat_with_user(user_message, chat_history)
    print(f" A I > {ai_message}")    