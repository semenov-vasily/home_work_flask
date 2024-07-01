# Домашнее задание "Flask"

## `Порядок работы`

1. Запускаем Docker Desktop. В терминале выполняем команду

>   `docker-compose up`

создается база данных


2. Запускаем файл [models.py](models.py), в базе данных создаются таблицы.

3. Запускаем файл [server.py](server.py), запускается приложение.

4. Открываем файл [client.py](client.py)

5. Используем закомментированный код сперва для создания пользователя(пользователей).
Пользователя можно создать, вывести данные о нем, изменить имя и пароль пользователя,
удалить пользователя.

6. Далее можно создать объявление(объявления), привязанное к конкретному пользователю.
Можно вывести данные об объявлении, изменить название, текст и пользователя, а так же 
удалить объявление.

7. При удалении пользователя все привязанные к нему объявления удаляются.



# Домашнее задание к лекции «Flask»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория. 

## Задание 1

Вам нужно написать REST API (backend) для сайта объявлений.

Должны быть реализованы методы создания/удаления/редактирования объявления.    

У объявления должны быть следующие поля: 
- заголовок
- описание
- дата создания
- владелец

Результатом работы является API, написанное на Flask.

Этапы выполнения задания:

1. Сделайте роут на Flask.
2. POST метод должен создавать объявление, GET - получать объявление, DELETE - удалять объявление.
