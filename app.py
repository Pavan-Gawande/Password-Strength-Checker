from flask import Flask, request, render_template
from checker import PasswordChecker

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def index():
    password = strength = crack_time = None
    if request.method == 'POST':
        password = request.form['password']
        checker = PasswordChecker(password)
        strength, crack_time = checker.check_strength()
    return render_template('index.html',password=password, strength=strength, crack_time=crack_time)

if __name__ == '__main__':
    app.run(debug=True)

