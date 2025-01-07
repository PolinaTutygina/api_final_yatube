# api_final
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/yandex-praktikum/api_final.git
cd api_final

Cоздать и активировать виртуальное окружение:
python -m venv venv
source venv/bin/activate

Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python manage.py migrate

Запустить проект:
python manage.py runserver