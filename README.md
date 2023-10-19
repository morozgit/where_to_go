# Куда сходить

Интерактивная карта активного отдыха Москвы. 
## Установка 

Установите [python3](https://realpython.com/installing-python/).

## Репозиторий
Клонируйте репозиторий в удобную папку.

## Виртуальное окружение
В терминале перейдите в папку с репозиторием.

### Создание виртуального окружения
```python 
python3 -m venv venv
```

### Активация виртуального окружения

```
source venv/bin/activate
```
### Переменные окружения
```python
echo SECRET_KEY=ваш SECRET_KEY > .env
echo ALLOWED_HOSTS=ваш SECRET_KEY >>.env
echo DEBUG=False >>.env
```

ALLOWED_HOSTS [см документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

DEBUG — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
### Установка библиотек

```python 
pip3 install -r requirements.txt
```

## Ссылки 
[Сайт](http://morozec76.pythonanywhere.com/).

[Административная панель](http://morozec76.pythonanywhere.com/admin).
Для входа требуется логин и пароль


## Загрузка данных из json

Из директории с проектом запустите сайт командой.
```python
python3 manage.py load_place ссылка на json
```

[Пример json файла](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9F%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D0%BA%D0%B0%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%B2%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9%20%D0%BD%D0%B0%2060-%D0%BC%20%D1%8D%D1%82%D0%B0%D0%B6%D0%B5%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0-%D0%A1%D0%B8%D1%82%D0%B8.json)
## Запуск
### Создание базы данных 
```python
python3 manage.py makemigrations
python3 manage.py migrate
```
### Создание суперпользователя
```python
python3 manage.py createsuperuser
```
### Запуск сервера
```python
python3 manage.py runserver
```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
