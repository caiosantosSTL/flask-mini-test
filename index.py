from flask import Flask, redirect, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/index')
def index():
    success_message = request.args.get('success_message', '')
    return render_template('index.html', success_messagex=success_message)

@app.route("/person/<name>")
def my_name(name):
    return f"Hello, {escape(name)}!"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

# ------------- formulario post

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    info = request.form['info']
    print(f'Informações recebidas: {info}')
    return redirect(url_for('index', success_message='Dados enviados com sucesso!'))
    #return 'Informações recebidas com sucesso!'

# -----------------------

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

