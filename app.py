import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import flash, redirect, url_for
from werkzeug.security import generate_password_hash
from forms import RegistrationForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'BURN_BUTCHER_BURN'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # --- ДОДАЙТЕ ЦЕЙ МЕТОД ---
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f'<User {self.username}>'

# Тепер це глобальний список, доступний для всіх функцій
PROJECTS = [
    {
        'slug': 'project-aurora',
        'title': 'Корпоративний сайт "Aurora"',
        'category': 'Frontend / UI-UX',
        'image_filename': 'portfolio_placeholder_1.jpg',
        'description': 'Це детальний опис проєкту Aurora. Ми розробили яскравий та сучасний дизайн, зверстали адаптивні сторінки та налаштували анімації для кращого користувацького досвіду.'
    },
    {
        'slug': 'project-cybershell',
        'title': 'Панель адміністратора "Cybershell"',
        'category': 'Flask / Backend',
        'image_filename': 'portfolio_placeholder_2.jpg',
        'description': 'Розробка потужного бекенду для панелі адміністратора. Спроєктовано базу даних, створено REST API для взаємодії з фронтендом, реалізовано систему аутентифікації.'
    },
    {
        'slug': 'project-nova',
        'title': 'Мобільний додаток "Nova"',
        'category': 'Flutter',
        'image_filename': 'portfolio_placeholder_3.jpg',
        'description': 'Кросплатформенний мобільний додаток, написаний на Flutter. Дозволяє користувачам обмінюватися фотографіями та короткими повідомленнями в режимі реального часу.'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    # ... (тут ваш код для сторінки "Про команду", його не чіпаємо)
    team_members = [
        {'name': 'Михайло', 'nickname': 'CaptainCode', 'role': 'Team Lead / Architect', 'contact_link': 'https://t.me/your_telegram_nick_1'},
        {'name': 'Анна', 'nickname': 'Glitch', 'role': 'Frontend Developer / UI-UX', 'contact_link': 'https://t.me/your_telegram_nick_2'},
        {'name': 'Олексій', 'nickname': 'Socket', 'role': 'Backend Developer', 'contact_link': 'https://t.me/your_telegram_nick_3'}
    ]
    return render_template('about.html', team=team_members)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=PROJECTS)

@app.route('/portfolio/<string:project_slug>')
def project_detail(project_slug):
    # Шукаємо потрібний проєкт у списку PROJECTS за його 'slug'
    found_project = None
    for project in PROJECTS:
        if project['slug'] == project_slug:
            found_project = project
            break
    
    # Передаємо дані знайденого проєкту у новий шаблон
    return render_template('project_detail.html', project=found_project)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Хешуємо пароль, щоб не зберігати його у відкритому вигляді
        hashed_password = generate_password_hash(form.password.data)
        
        # Створюємо нового користувача
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        
        # Додаємо його в базу даних
        db.session.add(user)
        db.session.commit()
        
        # Показуємо повідомлення про успіх і перенаправляємо на головну
        flash('Вітаємо, ви успішно зареєструвалися!', 'success')
        return redirect(url_for('home'))
        
    return render_template('register.html', title='Реєстрація', form=form)


if __name__ == '__main__':
    app.run(debug=True)