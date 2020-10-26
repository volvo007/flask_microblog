from app import app # 第二个 app 是 init文件里的app 对象

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world'