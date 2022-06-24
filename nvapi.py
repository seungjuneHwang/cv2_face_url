import urllib.request

client_id = ""
client_secret = ""

def news(keyword):
    ret = ''
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        ret = response_body.decode('utf-8')
    else:
        # print("Error Code:" + rescode)
        ret = "Error Code:" + rescode

    return ret  # 결과값을 함수 밖으로 전달