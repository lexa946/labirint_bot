# Лабиринт страха
### Телеграм бот [Игра-Квест](https://t.me/labirint_fear_bot "ссылка на бота")

![Title Screen](title_screen.png)

Используемый стек технологий:
-
- **[python 3.12](https://www.python.org/downloads/)**
- **[SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/intro.html#documentation-overview)**
- **[Telegram BOT](https://core.telegram.org/bots/api)**
- **[Postgresql](https://www.postgresql.org/)**
- **[FastAPI](https://fastapi.tiangolo.com/ru/tutorial/)**

Библиотеки:
-
- sqlalchemy
- sqladmin
- pydantic-settings
- pydantic
- aiogram
- asyncpg
- alembic
- fastapi
- uvicorn



FastAPI, uvicorn и sqladmin нужны исключительно, чтобы можно было запустить локально админку и быстро подредачить что-то в БД.

## Об игре
Когда вы читаете книгу не посещала ли вас мысль, что было бы интересно, если бы я сам мог решать, куда дальше пойдет мой персонаж.
В этой игре как раз это и лежит в задумке автора. Вам предстоит пройти по лабиринту, набитому самыми разными ловушками, испытаниями и врагами. 
Только вам решать куда идти дальше.

## От разработчика
Для запуска проекта необходимо в корне создать файл .env \
В файл добавить следующие настройки:
- **BOT_TOKEN** - токен вашего бота
- **ADMIN_ID** - ваш ID в телеграме. Когда бот запустится, он вам напишет. 
- **DB_USER** - Имя пользователя от БД
- **DB_PASS** - Пароль от БД
- **DB_NAME** - Название самой БД
- **DB_HOST** - Хост БД
- **DB_PORT** - Порт БД

### TODO
1. Прописать битвы с боссами
2. Доделать систему отступлений
