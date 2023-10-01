from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    dob = request.form.get('dob')
    
    if not name:
        return "Name is required. Please go back and enter your name."

    if not dob:
        return "Date of birth is required. Please go back and enter your date of birth."

    try:
        dob_parts = dob.split('-')
        birth_year = int(dob_parts[0])
        today_year = date.today().year
        age = today_year - birth_year
        birth_date = date(birth_year, int(dob_parts[1]), int(dob_parts[2]))
        day_of_week = birth_date.strftime('%A')
    except ValueError:
        return "Invalid date format. Please enter a valid date in 'yyyy-mm-dd' format."

    return render_template('result.html', name=name, age=age, day_of_week=day_of_week)

if __name__ == '__main__':
    app.run(debug=True)