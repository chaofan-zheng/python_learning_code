######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
 #     > Mail: 250919354@qq.com 
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, render_template,send_file


app = Flask(__name__)

@app.route('/about',methods=['GET', 'POST'])
def about():
    return send_file('templates/about.html')

@app.route('/index',methods=['GET', 'POST'])
def index():
    return send_file('templates/index.html')

@app.route('/codes',methods=['GET', 'POST'])
def codes():
    return send_file('templates/codes.html')

@app.route('/contact',methods=['GET', 'POST'])
def contact():
    return send_file('templates/contact.html')

@app.route('/gallery',methods=['GET', 'POST'])
def gallery():
    return send_file('templates/gallery.html')

@app.route('/icons',methods=['GET', 'POST'])
def icons():
    return send_file('templates/icons.html')



if __name__ == '__main__':
    app.run(debug=True)

