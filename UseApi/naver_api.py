import urllib.request
import json
client_id = ""
client_secret = ""

# 번역할 메모장 불러오기
with open('source.txt','r',encoding='utf8') as f:
    srcText = f.read()

encText = urllib.parse.quote(srcText)
data = "source=ko&target=es&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    # json 형 변환
    res = json.loads(response_body.decode('utf-8'))
    from pprint import pprint
    pprint(res)

    # 파일 생성
    with open('translate.txt', 'w',encoding='utf8') as f:
        f.write(res['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)