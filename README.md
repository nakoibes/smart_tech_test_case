# Тестовое задание для Смарт Текнолоджис
Веб-сервис позволяет выполнить разворот строки и перестановку четных и нечетных символов. Непосредственные операции со строками происходят в фоновом режиме. Для локального запуска и хранения данных о задаче используется база данных MongoDB, также сервис можно собрать в Docker, там используется база данных MongoDB.
В базе данных хранится сущность **Task**, которая имеет следующие поля:
* **id** - уникальный идентификатор задачи
* **type** - тип выполняемой задачи
* **text** - содержание строки
* **result** - результат выполнения задачи
* **status** - статус выполнения задачи


Также реализован клиент для взаимодействия с сервером, с помощью которого можно:
```bash
pip install -r requirements.txt
cd client
```
### Получить инструкцию по работе клиента
Запрос
```bash
python3 client.py --help
```

### Загрузить задачу
Запрос
```bash
python3 client.py --port 8000 --action CREATE --type REVERSE --text qwerty
```
Ответ: id созданной задачи или http код ошибки

### Проверить статус выполнения задачи
Запрос
```bash
python3 client.py --port 8000 --action GETSTATUS --id 54ea48f24b4140d5b2eb061a7c7c3b15
```
Ответ: статус выполнения задачи

### Проверить результат выполнения задачи
Запрос
```bash
python3 client.py --port 8000 --action GETRESULT --id 54ea48f24b4140d5b2eb061a7c7c3b15
```
Ответ: результат выполнения задачи<br>

Проект поддерживает сборку в Docker
* Клонируем проект
```bash
sudo docker-compose up -d
```

Для локальной работы без Docker, необходимы python 3.8+, MongoDB.
* Клонируем проект
* Создаем виртуальное окружение 
```bash
python -m venv venv
```
* Активируем виртуальное окружение
```bash
source venv/bin/activate
```
* Устанавливаем зависимости из requirements.txt
* ```bash
pip install -r requirements.txt
```
* Устанавливаем переменные окружения
```bash
export FLASK_APP=wsgi.py
```
* Запускаем http сервер командой flask run, и в другом окне терминала(с включенным виртуальным окружением)<br>

В корне лежит скрипт test.py с тестом

При локальном запуске api доступно на порту 5000, при  запуске из Docker
на порту 8000
