from flask import Flask
from flask import jsonify

app = Flask(__name__)

# default page output!
@app.route("/")
def index():
    return "Welcome in CS411!"

# A simple function to calculate the square of a number
@app.route('/sqr/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

if __name__ == "__main__":
    app.run(debug=True)
