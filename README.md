# Создаем папку для проекта
mkdir portfolio_project
cd portfolio_project

# Создаем виртуальное окружение
python3 -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate

# Устанавливаем Django
pip install django

# Дополнительные полезные пакеты
pip install pillow  # для работы с изображениями

# Создаем проект
django-admin startproject portfolio .

# Создаем приложение для портфолио
python manage.py startapp main

# Создаем миграции
python manage.py makemigrations

# Применяем миграции
python manage.py migrate

# Создаем суперпользователя
python manage.py createsuperuser

# Запускаем сервер
python manage.py runserver

# Создание папок для статических файлов
mkdir static media templates

# Сбор статических файлов (когда будет готово для продакшена)
python manage.py collectstatic

# Для деплоя можно использовать:
# bash
# Установка Gunicorn
pip install gunicorn

# Установка Nginx
sudo apt install nginx


# Для продакшена
При деплое на сервер:

Создайте .env на сервере с продакшен значениями:

SECRET_KEY=ваш-продакшен-ключ
DEBUG=False
ALLOWED_HOSTS=ваш-домен.ru,www.ваш-домен.ru
Убедитесь, что .env не попадает в git