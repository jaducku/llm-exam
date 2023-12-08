import os
import openai

os.environ["OPENAI_API_KEY"] = "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" # 환경변수에 OPENAI_API_KEY를 설정합니다.
openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = """
넌 유능한 통역사야. 처음 상대방이 인사를 하면 동일한 언어로 인사를 건내고 어느나라 말로 통역할지 물어본 후 답변을 받으면 그 말로 통역을 해줘.
"""

def openai_llm(input_text, chat_history):

    if len(chat_history) == 0:
        chat_history.append({"role": "system", "content": system_prompt})

    chat_history.append({"role": "user", "content": input_text})

    completion = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                messages=chat_history)

    output = completion.choices[0].message.content

    chat_history.append({"role": "assistant", "content": output})

    #print(chat_history)

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