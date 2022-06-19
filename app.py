from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from a Flask app</h2>'

# greeting message
@app.route('/<username>')
def show_user(username):
    # Greet the user
    return f'Hello {username} !'

if __name__ == "__main__":
    app.run(debug=True)
