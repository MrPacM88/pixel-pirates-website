from flask import Flask, render_template

app = Flask(__name__)
@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    # У майбутньому ми зможемо завантажувати ці дані з бази даних
    team_members = [
        {'name': 'Капітан Джек', 'role': 'Team Lead / Full-Stack', 'avatar': 'avatar_placeholder.png'},
        {'name': 'Навігатор Анна', 'role': 'Frontend Developer / UI-UX', 'avatar': 'avatar_placeholder.png'},
        {'name': 'Боцман Олексій', 'role': 'Backend Developer', 'avatar': 'avatar_placeholder.png'}
    ]
    return render_template('about.html', team=team_members)

if __name__ == '__main__':
    app.run(debug=True)