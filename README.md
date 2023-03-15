# Grodno Street-O

Название проекта: Web site for Grodno Street-O

Автор: Natallia Kavalchuk

## О проекте:  
Сайт "Web site for Grodno Street-O" создан в качестве финального проекта курса Разработка web приложений 
на Python, IT-academy, г. Гродно

Данный проект создан с целью обобщения информации о серии открытых тренировок Grodno Street-O по спортивному 
ориентированию. Пользователь молучает всю необходимую информацю: календарь мероприятий, подробности о каждом из них 
отдельно, а также возможность зарегистрироваться.

В проекте реализована регистрация и авторизация пользователей, создание и удаление мероприятий, а также автоматическая 
регистрация пользователя на мероприятие.

Проект еще не завершен. Также планируется создать:

1. "Профиль пользователя", в котором будет отражаться статистика участия данного пользователя в серии стартов
2. Модификация страницы мероприятия: отображение списка зарегистрированных участников, статистика
3. Улучшение главной страницы: информационное оформление и сопровождение
4. Развитие дополнительного функционала, использование дополнительных сторонних библиотек для отображения функционала.

## Quick Start:
To get this project up and running locally on your computer follow the following steps.

1. Clone the repository https://github.com/NatalykaKavalchuk/my_final_proj.git
2. Set up a python virtual environment
3. Run the following commands
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

4. Open a browser and go to http://localhost:8000/
