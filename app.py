from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/a')
def a():
    return 'Hello, a!'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        # 이미지 url을 받기
        url = request.form["url"]
        # 관상 코드 실행
        return f"POST로 전달<br><img src='{url}'>"

if __name__ == '__main__':
    app.run(debug=True)