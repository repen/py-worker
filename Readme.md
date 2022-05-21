### Описание проекта 

Минимальный набор для создания различных скриптов на Python.

### Запуск

`python main.py --config production`

Параметры запуска

- `--config development` загрузить нужный конфиг который находится в файле `config.py`. По умолчанию стоит `default`.


### Docker

Можно запускать скрипт в докер контейнере. 

1. нужно сбилдить контейнер со скриптом выполнив команду `docker build -t script_image:latest .`.
2. запуск контейнера `docker run --name container_name -d script_image:latest`
