# Проект Django

Этот проект разработан на Django и предоставляет [Пользователям просматривать каталог игрушек, добавлять их в корзину покупок, оформлять заказы и осуществлять оплату. Администраторы имеют доступ к панели управления, где они могут добавлять новые товары, управлять заказами и отслеживать активность покупателей.].

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
 python manage.py loaddata fixtures/categoreies/category.json
 ```
 ```sh
 python manage.py loaddata fixtures/products/product.json
 ```
 ```sh
 python manage.py loaddata fixtures/users/user.json
 ```
 4. Запустите тестовый сервер:
  ```sh
 python manage.py runserver
 ```
5. Перейдите по ссылке: (http://127.0.0.1:8000)

## Тестовый суперпользователь
### login:igor password:igor
