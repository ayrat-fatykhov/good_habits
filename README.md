# Курсовая 7. DRF

## Запуск проекта
- Клонировать репозиторий
- Активировать виртуальное окружение (команда в терминале: source env/bin/activate)
- Установить зависимости (команда в терминале: pip3 install -r requirements.txt)
- Создать файл .env, заполнить его данными из файла .env.sample
- Создать базу данных в postresql
- Создать (команда в терминале: python manage.py makemigrations) и применить миграции (команда в терминале: python manage.py migrate)
- Создать суперпользователя командой python manage.py csu
- Запустить celery (команда в терминале: celery -A config worker -l INFO)
- Запустить проект python manage.py runserver

## Документация к API
- http://127.0.0.1:8000/redoc/
- http://127.0.0.1:8000/swagger/

## Примечание
Для отправки сообщения в телеграм боте необходимо для пользователя указать телеграм id.
При необходимости его можно указать в админке (ссылка: http://127.0.0.1:8000/admin).
Для уточнения своего телеграм id можно воспользоваться телеграм ботом userinfobot.