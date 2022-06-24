import func
import face
import nvapi
import json

# func.face('이미지 주소')

# 함수 호출
news = nvapi.news('불금')
print(news) # nvapi.news에서 전달된 데이터를 출력

# face.face_func('https://cdn.mindgil.com/news/photo/202201/73470_12193_834.png')