import openai

# OpenAI API key를 설정합니다.
openai.api_key = "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"

# 사용자로부터 지시사항을 입력받습니다.
while True:
    prompt = input("지시사항을 입력하세요 : ")
    
    # "quit"을 입력하면 프로그램을 종료합니다.
    if prompt == "quit": 
        break

    # OpenAI API를 사용하여 입력받은 지시사항에 대한 응답을 생성합니다.
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["너:"]
    )

    # 생성된 응답 중 첫 번째 응답을 출력합니다.
    print(response["choices"][0]["text"].strip())