# Currency-parser-Kokos-group-test

### Описание
Собирает курсы валют с сайта.

### Технологии

[![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.6-blue?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/DjangoRestFramework-3.15.1-blue?style=flat)](https://pypi.org/project/djangorestframework/)
---

### Запуск проекта
- Клонируйте репозиторий с проектом на свой компьютер
```bash
git clone https://github.com/Luna-luns/Currency-parser-Kokos-group-test.git
```

- Установите и активируйте виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate
```

- Установите зависимости из файла requirements.txt

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### Выполните миграции и создайте суперпользователя:
```bash
python3 manage.py migrate
python3 manage.py createsuperuser
```

### Заполните базу данными: 
```bash
python3 manage.py upload_data
```

### Логин и пароль администратора:
```bash
admin
admin-admin4
```

### Пример получения курсов валют
```bash
[
    {
        "currency": "AUD",
        "value": 60.4411
    },
    {
        "currency": "AZN",
        "value": 53.9018
    },
    {
        "currency": "GBP",
        "value": 114.6146
    }
]
```

## 🚀 Разработчик
[Струнникова Елизавета](https://github.com/Luna-luns)<br>
Email: liza.strunnikova@yandex.ru<br>
Telegram: @l_lans
