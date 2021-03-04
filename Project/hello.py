from flask import Flask

app = Flask(__name__)


# 告诉相应url应该调用那个函数
# / 与 hello_world 函数绑定，options里面传参数
@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello {name}'


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


if __name__ == '__main__':
    app.run(debug=True)

# terminal 中执行 python3 hello.py 就启动了一个简单的flask
