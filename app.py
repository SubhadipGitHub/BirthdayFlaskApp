from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Placeholder for poll results
poll_results = {
    'kind': 0,
    'funny': 0,
    'smart': 0,
    'beautiful': 0
}

@app.route('/')
def countdown():
    return render_template('countdown.html')

@app.route('/birthday')
def birthday():
    birthday_message = "Happy Birthday to the most wonderful person in my life. You light up my world and make every day special. I love you more than words can express."
    return render_template('birthday.html', message=birthday_message, gif_url=url_for('static', filename='img/birthday.gif'))

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    global poll_results
    if request.method == 'POST':
        choice = request.form.get('characteristic')
        if choice in poll_results:
            poll_results[choice] += 1
        return redirect(url_for('poll_results'))
    return render_template('poll.html')

@app.route('/poll_results')
def poll_results_page():
    global poll_results
    return render_template('poll_results.html', poll_results=poll_results)

def is_birthday():
    today = datetime.today()
    birthday = datetime(today.year, 8, 1)  # Replace with your fiancée's birthday
    return today.date() == birthday.date()

@app.before_request
def redirect_to_birthday():
    if is_birthday():
        return redirect(url_for('birthday'))

if __name__ == '__main__':
    app.run(debug=True)
