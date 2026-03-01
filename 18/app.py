# Program 18: Flask Calculator using AJAX
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    else:
        result = "Invalid"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)