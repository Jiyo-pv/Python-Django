# Program 19: Suggestion Form using AJAX
# @JIYO P V ROLL NO:33 Date: 01-03-2026

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    # Just returning response (no database needed for basic version)
    return jsonify({'response': f"Thank you {name} for your suggestion!"})

if __name__ == '__main__':
    app.run(debug=True)