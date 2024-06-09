# Курсовая 8. Docker

## Запуск проекта на локальном сервере
После клонирования проекта из репозитория, активации виртуального окружения и установки всех зависимостей через ввести в терминале:
- sudo docker-compose build
- docker-compose up (проект будет доступен по адресу http://0.0.0.0:8001)

## Деплой проекта
Команды в терминале:
- ssh имя_пользователя@айпи_адрес (имя_пользователя и айпи_адрес выдаются после создания виртуальной машины)
- ssh-copy-id имя_пользователя@айпи_адрес
- apt update
- apt install nginx python3-venv postgresql postgresql-contrib git
- git clone <ссылка на репозиторий> (для клонирования необходимо на платформе гит прописать ssh ключ; его можно получить, написав в терминале ssh-keygen и cat /root/.ssh/id_rsa.pub)
- cd good_habits
- python3 -m venv env
- source env/bin/activate
- pip3 install -r requerements.txt
- pip3 install gunicorn
- psql -U postqres -> create database good_habits; (перед этой командой необходимо в файле /etc/postgresql/14/main/pg_hba.conf параметр peer установить на trust)
- nano /etc/systemd/system/good_habits.service (прописать внутри содержимое Текст1)
- systemctl start good_habits
- nano /etc/nginx/sites-available/good/habits (прописать внутри содержимое Текст2)
- ln -s /etc/nginx/sites-available/good/habits /etc/nginx/sites-enabled/
- systemctl restart nginx

## Текст1
[Unit]
Description=good_habits daemon
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/html/good_habits/
ExecStart=/var/www/html/good_habits/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/html/good_habits/good_habits.sock config.wsgi

[Install]
WantedBy=multi-user.target)

## Текст2
server {
    listen 80;
    server_name <айпи_адрес виртуальной машины>;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /var/www/html/good_habits;
    }

    location /media/ {
        root /var/www/html/good_habits;
    }


    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/html/good_habits/good_habits.sock;
    }
}

## Примечание
Проект загружен и работает по адресу: http://2.56.89.61


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

## Примечания
- Для отправки сообщения в телеграм боте необходимо для пользователя указать телеграм id.
При необходимости его можно указать в админке (ссылка: http://127.0.0.1:8000/admin).
Для уточнения своего телеграм id можно воспользоваться телеграм ботом userinfobot.
- Результаты тестирования сохранены в файле coverage.txt

