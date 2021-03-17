# emphasoft-test
Тестовое задание в EmphaSoft

Регистрация пользователей через **SocialAuth** 
с помощью Google+ и Github OAuth2, включая классическую регистрацию.
После регистрации пользователь может заполнить профиль с личной информацией,
загрузить аватар и сохранить это все. 
На главной странице выведена таблица со списком всех пользователей.

# Локальный запуск
* Склонировать репозиторий
    * ```git clone https://github.com/plaunezkiy/emphasoft-test.git```
    
    
* Создать среду и установить зависимости
    * ```python -m venv venv```
    * ```. /venv/bin/activate``` или ```. /venv/scripts/activate```
    * ```pip install -r requirements.txt```


* Создать файл .env и указать в нем: ключи авторизации для приложений 
Github и Google, SECRET_KEY для Django
    * **SECRET_KEY**
    * **SOCIAL_AUTH_GITHUB_KEY**
    * **SOCIAL_AUTH_GITHUB_SECRET** 
    * **SOCIAL_AUTH_GOOGLE_OAUTH2_KEY**
    * **SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET**


* Применить миграции, запустить сервер и радоваться жизни :-)
    * ```./manage.py migrate```
    * ```./manage.py runserver```