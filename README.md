# Урок 27_2


## Установите Docker и Docker Compose:

* Установите Docker, следуя инструкциям для вашей операционной системы: [Docker Install](https://docs.docker.com/get-docker/).
* Установите Docker Compose: [Docker Compose Install](https://docs.docker.com/compose/install/).

## Создайте файл .env-non-dev:

* Создайте файл .env-non-dev в той же директории, где находится ваш файл docker-compose.yml. В этом файле укажите все необходимые переменные окружения для ваших сервисов (например, базы данных, Redis, вашего приложения и Celery).
## Запустите приложение:

* Откройте терминал в директории с файлом docker-compose.yml.
* Выполните следующую команду:
    ```bash
        docker-compose up --build
Docker Compose загрузит образы, создаст и запустит контейнеры для ваших сервисов.
## Проверьте приложение:

После успешного запуска, ваше приложение LMS должно быть доступно по адресу http://localhost:7777.
## Остановите приложение:

* В терминале, где была запущена команда docker-compose up, нажмите Ctrl+C для остановки контейнеров.