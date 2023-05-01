# yandex-afisha-clone

Это backend часть для [frontend](https://github.com/devmanorg/where-to-go-frontend/). Пример работающего сайта представлен на этом [сайте](https://testserverdvmn.pythonanywhere.com/)

## Установка

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip download --destination-directory DIR -r requirements.txt
```

В конце сгенерируёте секретный ключ `secret_key`, в котором будет не меньше 50 символов и не меньше 5 уникальных символов, создайте локальную переменную командой `SECRET_KEY="secret_key"` и экспортируёте его во внешнее пространство командой: `export SECRET_KEY`.

## Пройстой запуск

Чтобы запустить backend нужно:
1. положить все статичные файлы (весь [frontend](https://github.com/devmanorg/where-to-go-frontend/)) в директорию `asserts`,
2. создайте директории `media` и `static` в корне проекта,
3. выполните команду `python3 manage.py migrate`,
4. выполните команду `python3 manage.py collectstatic`,
5. находясь в корневой директории запустить backend командой: `python3 manage.py runserver --insecure`,
6. перейдите на сайт http://127.0.0.1:8000/

Для работы с БД:
1. создате суперпользователя командой `python manage.py createsuperuser`,
2. пройдите все шаги,
3. выполните команду `python3 manage.py migrate`,
2. выполните команду `python3 manage.py collectstatic`,
4. запустите сервер `python3 manage.py runserver --insecure`,
5. перейдите на сайт http://127.0.0.1:8000/admin
6. войдите под своими установленными логином и паролем

## Параметры для дальнейшего развёртывания

Для дальнейшего развёртывания требуется определить в области видимых перменных командой `export` следуюшие переменные:
1. `DEBUG` - установить любое значение чтобы установить в `True`, иначе будет установлено в `False`,
2. `ALLOWED_HOSTS` - установить доступные для подключения хосты через запятую в формате `host_1,host_2`, по умолчанию устанавливается в `.localhost,127.0.0.1,[::1]`,
3. `SECURE_HSTS_SECONDS` - установить время в секундах в формате целого положительного числа, по умолчанию устанавливается в "0".
4. `SECURE_HSTS_INCLUDE_SUBDOMAINS` - установить любое значение чтобы установить в `True`, иначе будет установлено в `False`,
5. `SECURE_HSTS_PRELOAD` - установить любое значение чтобы установить в `True`, иначе будет установлено в `False`,
6. `SECURE_SSL_REDIRECT` - установить любое значение чтобы установить в `True`, иначе будет установлено в `False`,
7. `SESSION_COOKIE_SECURE` - установить любое значение чтобы установить в `True`, иначе будет установлено в `False`,
8. `CSRF_COOKIE_SECURE` - установить любое значение чтобы установить в `True`, иначе будет установлено в `False`.

Другие настройки смотрите в [документации](https://docs.djangoproject.com/en/4.2/ref/settings/).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
