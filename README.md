# Система управления заказами в кафе

_Полнофункциональное веб-приложение для управления заказами в кафе с встроенным API._

_Это приложение предоставляет удобный инструмент для управления заказами в кафе, автоматизации процессов и повышения эффективности работы персонала._

---

## Основной функционал

### 1. **Отображение всех заказов**

- Отображает ID заказа, номер стола, список блюд, общую стоимость и статус заказа.

### 2. **Добавление заказа**

- Возможность создания нового заказа с указанием номера стола и списка блюд.
- Система автоматически присваивает уникальный ID, рассчитывает стоимость и устанавливает статус "В ожидании".

### 3. **Удаление заказа**

- Функция для удаления заказа из системы.

### 4. **Поиск заказа**

- Функция поиска заказов через поисковую строку по номеру стола или статусу.

### 5. **Изменение заказа**

- Функция для изменения статуса заказа и списка блюд.

### 6. **Расчет выручки за смену**

- Функция расчета общей выручки за все заказы со статусом "Оплачено".

### 7. **Фильтрация заказов**

- Функция фильтрации заказов по их статусу (например, "В ожидании", "Готово", "Оплачено").

### 8. **Стол**

- Функция создания стола
- Функция просмотра списка всех столов
- Функция просмотра стола
- Функция изменения стола
- Функция удаления стола

### 9. **Блюдо**

- Функция создания блюда
- Функция просмотра списка всех блюд
- Функция просмотра блюда
- Функция изменения блюда
- Функция удаления блюда

---

## Технологии и зависимости

- **Язык программирования:**  
  Python 3.12

- **Фреймворки и библиотеки:**
    - Django 5.1.6
    - Django REST Framework 3.15.2
    - Django Filter 25.1
    - DRF-YASG 1.21.8 (для документации API)

- **База данных:**
    - PostgreSQL (с использованием psycopg2-binary 2.9.10)

- **Дополнительные инструменты:**
    - python-dotenv 1.0.1 (для управления переменными окружения)
    - gunicorn 23.0.0 (для запуска веб-сервера)

---

## Архитектура приложения

1. **Модели данных:**
    - #### Заказ (Order):
        - Поля: ID, номер стола, список блюд, общая стоимость, статус.
    - #### Стол (Table):
        - Поля: ID, номер, количество мест.
    - #### Блюдо (Dish):
        - Поля: ID, название, цена.


2. **API:**
    - #### Заказ
        - `GET api/orders/` — список всех заказов.
        - `POST api/orders/` — создание нового заказа.
        - `GET api/orders/{id}/` — детализация заказа.
        - `PUT api/orders/{id}/` — изменение заказа.
        - `DELETE api/orders/{id}/` — удаление заказа.
        - `GET api/orders/revenue/` — расчет выручки за смену.
        - `GET api/orders/filter/` — фильтрация заказов по статусу.
    - #### Стол
        - `GET api/tables/` — список всех столов.
        - `POST api/tables/` — создание нового стола.
        - `GET api/tables/{id}/` — детализация стола.
        - `PUT api/tables/{id}/` — изменение стола.
        - `DELETE api/tables/{id}/` — удаление стола.
    - #### Блюдо
        - `GET api/dishes/` — список всех столов.
        - `POST api/dishes/` — создание нового стола.
        - `GET api/dishes/{id}/` — детализация стола.
        - `PUT api/dishes/{id}/` — изменение стола.
        - `DELETE api/dishes/{id}/` — удаление стола.


3. **Веб-интерфейс:**
    - Таблица заказов с возможностью сортировки и фильтрации.
    - Таблицы столов и блюд.
    - Экран подсчета выручки.
    - Экраны всего механизма CRUD для заявки, стола и блюд.
    - Поисковая строка для быстрого поиска заказов по номеру стола и статусу.

## Документация API
- Подробная документация API доступна по эндпоинту `/swagger/`.

## Админ-панель
- Админ-панель доступна по эндпоинту `/admin/`

---

## Установка и запуск

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/GromovAS21/order_management_service.git
   cd order_management_service
   ```
2. **Установка зависимостей**

- Установите зависимости с помощью Poetry и активируйте виртуальное окружение:
    ```bash
    poetry install
    poetry shell
    ```

3. **Настройка переменных окружения**

- Переименуйте файл [.env.sample](.env.sample) в [.env](.env.sample) и заполните все переменные в этом файле.

4. **Создание базы данных и ее заполнение**

- Создайте базу данных PostgreSQL;
- Примените после этого команду для применения миграций:
     ```bash
     python3 manage.py migrate
     ```

5. **Создание суперпользователя**
    ```bash
    python3 manage.py csu
    ```
   
6. **Запуск Docker контейнера**
     ```bash
   docker-compose up -d --build
     ```

#### Веб-приложение будет доступно по адресу: http://127.0.0.1

---

## Pre-commit
В проекте присутствует функция pre-commit, который проверяет код на соответствие стандартам PEP8 состоящие из isort, black, flake8;

**Запуск Pre-commit**
```bash
pre-commit install
git add .pre-commit-config.yaml
```
После этого при попытке создания коммита будет запускаться проверка кода и если все проверки проходят, создается коммит.

Для ручной проверки кода необходимо выполнить команду:
```bash
pre-commit run --all-files
```

#### ВАЖНО!!! ####
Перед коммитом необходимо выполнить одну из следующих команд:
```bash
git add . # Добавляет все файлы в индекс
```
```bash
git add <file_name> # Добавляет указанный файл в индекс
```

---

## Тесты
Покрытие тестов составляет 93%

**Запуск Тестов**
```bash 
docker-compose exec -it <container_id> poetry run coverage run manage.py test
docker-compose exec -it <container_id> poetry run coverage report
```

---

## Цитата
>"Аккуратный программист — быстрый программист"* - Билл Гейтс

---

Приятного использования! 🚀



