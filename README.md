# fonbet_parser

Скачать репозиторий проекта:
git clone https://github.com/AndrewFekl/fonbet_parser.git

Установка виртуального окружения:
Python -m venv env
env\scripts\activate (Windows)
pip install -r requirements.txt

Пакет проекта содержит файлы parsers.py и selenium_test.py

python parsers.py - запускает программу парсинга сайта и получает словарь всех футбольных матчей в Live

python selenium_test.py - импортирует parsers из пакета, получает название последнего матча из словаря,
открывает ссылку на него на сайте fonbet.ru/live и выдает в консоль название лиги/дивизиона.