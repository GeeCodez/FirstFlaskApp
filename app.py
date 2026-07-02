from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('name.html')

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:id>')
def show_post(id):
    return f'This post has the id {id}'

if __name__ == '__main__':
    app.run(debug=True)