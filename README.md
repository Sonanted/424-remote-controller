# 424-remote-controller
## Описание
Веб-приложение для лаборатории №424 МИЭМ НИУ ВШЭ, позволяющее работать с лабораторным стендом 

## Установка и запуск:
### создать виртуальное окружение на питоне:
```bash
python -m venv venv
```
### активировать его:
для Windows:
```bash
.\venv\Scripts\activate
```
для Linux:
```bash
source venv/Scripts/activate
```
### установить необходимые библиотеки:
```bash
pip install -r requirements.txt
```

### Принять миграции и собрать статику
```bash
python manage.py migrate
python manage.py collectstatic --no-input 
```

### Запустить приложение
```bash
python manage.py runserver
```
