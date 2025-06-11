from flask import Flask, render_template

app = Flask(__name__)

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

# НОВИЙ ДИНАМІЧНИЙ МАРШРУТ
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


if __name__ == '__main__':
    app.run(debug=True)