# Todo List API

Это небольшое веб-приложение на Flask, которое предоставляет RESTful API для управления списком задач (TODO list).

### Содержание
[TOC]

## Возможности

1. Создание задачи:
    - Метод: POST
    - URL: `/tasks/`
    - Параметры запроса: JSON-объект с полями `title` (строка) и `description` (строка, опционально).
    - Ответ: JSON-объект с полями `id`, `title`, `description`, `created_at`, `updated_at`.

2. Получение списка задач:
    - Метод: GET
    - URL: `/tasks/`
    - Ответ: JSON-список задач, где каждая задача представляет собой JSON-объект с
      полями `id`, `title`, `description`, `created_at`, `updated_at`.

3. Получение информации о задаче:
    - Метод: GET
    - URL: `/tasks/<id>`
    - Ответ: JSON-объект с полями `id`, `title`, `description`, `created_at`, `updated_at`.

4. Обновление задачи:
    - Метод: PUT
    - URL: `/tasks/<id>`
    - Параметры запроса: JSON-объект с полями `title` (строка, опционально) и `description` (строка, опционально).
    - Ответ: JSON-объект с полями `id`, `title`, `description`, `created_at`, `updated_at`.

5. Удаление задачи:
    - Метод: DELETE
    - URL: `/tasks/<id>`
    - Ответ: Сообщение об успешном удалении.

## Установка и запуск

### Предварительные требования

- Python 3.12
- MySQL

### Шаги по установке

1. Клонируйте репозиторий:

```bash
git clone https://github.com/ваш-репозиторий/todo-app.git
cd todo-app
```

2. Создайте виртуальное окружение и активируйте его:

```shell
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

3. Установите зависимости:

```shell
pip install -r requirements.txt
```

4. Настройте базу данных:
   Создайте базу данных MySQL и настройте переменные окружения для подключения:
```shell
export DATABASE_URL='mysql+pymysql://user:password@localhost/todo_db'
```

5. Выполните миграции базы данных:

```shell
flask db upgrade
```

5. Запустите приложение:

```shell
flask run
```
Приложение будет доступно по адресу: http://localhost:5000/

## Тестирование
Чтобы запустить тесты, выполните следующую команду:

```shell
python -m unittest discover -s tests
```


## Документация API
Документация Swagger доступна по адресу: http://localhost:5000/
