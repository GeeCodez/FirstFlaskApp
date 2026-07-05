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

@app.route('/post/<int:id>')
def show_post(id):
    return f'This post has the id {id}'

def show_user(username):
    return f'Hello {username} !'
  
app.add_url_rule('/user/<username>', 'show_user', show_user)

if __name__ == '__main__':
    app.run(debug=True)