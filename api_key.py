# openai 라이브러리를 import 합니다.
import openai

# openai API key를 설정합니다.
openai.api_key = "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"

# 메시지 리스트를 초기화합니다.
messages = []

# 무한 루프를 시작합니다.
while True :
    # 사용자로부터 입력을 받습니다.
    user_content = input("user : ")

    # 만약 입력이 "quit"이면 루프를 종료합니다.
    if user_content == "quit": break

    # 사용자의 입력을 메시지 리스트에 추가합니다.
    messages.append({"role" : "user", "content" : f"{user_content}"})

    # openai의 ChatCompletion API를 사용하여 대화를 생성합니다.
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages = messages)
    
    # 생성된 대화 중에서 가장 최근의 대화를 가져옵니다.
    assistant_content = completion.choices[0].message["content"].strip()

    # 생성된 대화를 메시지 리스트에 추가합니다.
    messages.append({"role" : "assistant", "content" : f"{assistant_content}"})

    # 생성된 대화를 출력합니다.
    print(assistant_content)
    print(messages)
