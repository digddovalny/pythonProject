# Проект Django

Этот проект разработан на Django и предоставляет [описание проекта].

## Установка приложения

1. Установите зависимости:
```sh
pip install -r requirements.txt
```
2. Выполните миграции:
```sh
python manage.py migrate
```
 3. Загрузите тестовые данные в базу:
 ```sh
 python manage.py loaddata fixtures.json
 ```
 ```sh
 python manage.py loaddata category.json
 ```
 ```sh
 python manage.py loaddata user.json
 ```
 4. Запустите тестовый сервер:
  ```sh
 python manage.py runserver --settings=settings.local
 ```
5. Перейдите по ссылке: (http://127.0.0.1:8000)
