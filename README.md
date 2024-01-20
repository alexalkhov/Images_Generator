В проекте реализована генерация изображений на основе Stable Diffusision Api. Проект истользует Python 3.11, django 5.0.1
и шаблоны HTML со стилизацией bootstrap

для установки проекта:
разверните виртуальное окружение:
python3 -m venv/venv
source venv/bin/activate
установите зависимости:
pip install -r requierements.txt
выполните миграции:
python3 manage.py makemigrations
python3 manage.py migrate
пропишите ваш token stable diffusion api в файле .env
запустите сервер:
python3 manage.py runserver