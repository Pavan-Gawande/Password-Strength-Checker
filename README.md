# Password-Strength-Checker

This is a simple and effective Password Strength Checker with a web interface built using Flask. It allows users to input a password, analyze its strength, estimate the time it would take to crack, and display the result in a clean, visually appealing interface.

When a user enters a password and clicks "Check," the password is sent to the backend where the PasswordChecker class:

 • Checks its strength based on length and complexity

 • Calculates its position among all possible combinations

 • Estimates crack time by dividing the position by 1 billion guesses per second and converting the result into hours, days, and years

 • Displays the result on the webpage


## Tech Stack

 • Backend: Python, Flask

 • Frontend: HTML, CSS

 • Libraries: Flask only


## How to Run

1. Clone the repository:

git clone https://github.com/Pavan-Gawande/Password-Strength-Checker.git
cd password-checker


3. Install Flask:

pip install Flask


5. Run the Flask app:
python app.py


6. Open your browser and go to:
http://127.0.0.1:5000



## Author

This project was created by Pavan Gawande as a personal project to work with Python and Flask. The goal was to explore building a simple web application and implement basic password strength analysis.


