import sys

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    text = request.form.get('text')
    dynamic_text = f"You entered: {text}"
    return render_template('result.html', dynamic_text=dynamic_text)

if __name__ == '__main__':
    app.run(debug=True)