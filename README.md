# yandex-afisha-clone

Это backend часть для [frontend](https://github.com/devmanorg/where-to-go-frontend/). Пример работающего [сайта](https://testserverdvmn.pythonanywhere.com/).

## Установка

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip install --destination-directory DIR -r requirements.txt
```

В конце сгенерируёте секретный ключ `secret_key`, в котором будет не меньше 50 символов и не меньше 5 уникальных символов, создайте локальную переменную командой `SECRET_KEY="secret_key"` и экспортируёте его во внешнее пространство командой: `export SECRET_KEY`.

## Запуск на локальном сервере

Чтобы запустить backend нужно:
1. если нужно использовать другой frontend, то положить все статичные файлы в директорию `static`,
2. выполните команду `python3 manage.py migrate`,
3. выполните команду `python3 manage.py collectstatic`,
4. находясь в корневой директории запустить backend командой: `python3 manage.py runserver --insecure`,
5. перейдите на сайт http://127.0.0.1:8000/

Для работы с сайтом как суперпользователь:
1. создате суперпользователя командой `python manage.py createsuperuser`,
2. пройдите все шаги,
3. выполните команду `python3 manage.py migrate`,
2. выполните команду `python3 manage.py collectstatic`,
4. запустите сервер `python3 manage.py runserver --insecure`,
5. перейдите на сайт http://127.0.0.1:8000/admin
6. войдите под своими установленными логином и паролем

## Команда для загрузки данных в БД

При наличии ссылки на .json файл, данные из него можно легко поместить в БД при помощи доп команды: `python3 manage.py load_place "https://path/to/json/file.json"`, где по ссылке `https://path/to/json/file.json` хранится содержимое удалённого .json файла:
```json
{
    "title": "Останкинская телебашня",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e3b20361050ae13b3aaf7ddcef76e7c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/adc544d7acc9be889cfec73064bcfb06.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6338bf58897bb4bef5c6ef1483c357de.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e5efbafdfc29423e361df0ee81145b7.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/99c1cb7ba5ccf948767524876edf27c8.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/67b694871a431460745668d686770f54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/e6ef6f4f3a7df07cb8881d4ed0c44b6e.jpg"
    ],
    "description_short": "Останкинская телебашня — одна из главных достопримечательностей Москвы и символ отечественного  телерадиовещания. Здесь проводятся экскурсии с подъёмом на высоту более трёхсот метров, а уникальный мультимедийный комплекс знакомит посетителей с устройством этого удивительного сооружения. ",
    "description_long": "<p>За последнее время внутри башни многое изменилось. Теперь это не только главная точка  телерадиовещания  в стране, но и туристический комплекс, побывать в котором может любой желающий.</p><p>На экскурсиях посетители познакомятся с историей строительства этого чуда инженерной мысли и смогут узнать, с какими сложностями пришлось столкнуться его создателям. В башне устроен интерактивный мультимедийный комплекс, в который также можно попасть во время экскурсии. Здесь гости услышат о технологических особенностях башни, познакомятся с «квакшами» и картой гроз в Москве. Оказывается, башня умеет петь и танцевать, а её шпиль значительно отклоняется под порывами ветра. За этими отклонениями можно будет проследить в реальном времени. Участники экскурсии выяснят, почему башня не падает, и поучаствуют в формировании рейтинга своего любимого телеканала.</p><p>Также для посещения доступна площадка на высоте 85 метров, где видно все 145 тросов, придающих башне гибкость и устойчивость. А с площадки на высоте 337 метров можно полюбоваться на панораму Москвы. Гостей ждёт и легендарный ресторан «Седьмое небо». Его полы вращаются, описывая полный оборот за 50 минут.</p><p>Узнать подробности можно на <a class=\"external-link\" href=\"https://www.tvtower.ru/\" target=\"_blank\">официальном сайте</a>, <a class=\"external-link\" href=\"https://vk.com/tv_tower\" target=\"_blank\">ВКонтакте</a> и в <a class=\"external-link\" href=\"https://www.instagram.com/ostankino_tvtower/\" target=\"_blank\">Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.61171499999998",
        "lat": "55.81972699999998"
    }
}
```

## Параметры для дальнейшего развёртывания

Для дальнейшего развёртывания требуется определить в области видимых перменных командой `export` следуюшие переменные:
1. `DEBUG` - установить в `true` или `false`, если не установлено, то будет установлено в `False`,
2. `ALLOWED_HOSTS` - установить доступные для подключения хосты через запятую в формате `host_1,host_2`, по умолчанию устанавливается в `.localhost,127.0.0.1,[::1]`,
3. `SECURE_HSTS_SECONDS` - установить время в секундах в формате целого положительного числа, по умолчанию устанавливается в "0".
4. `SECURE_HSTS_INCLUDE_SUBDOMAINS` - установить в `true` или `false`, если не установлено, то будет установлено в `False`,
5. `SECURE_HSTS_PRELOAD` - установить в `true` или `false`, если не установлено, то будет установлено в `False`,
6. `SECURE_SSL_REDIRECT` - установить в `true` или `false`, если не установлено, то будет установлено в `False`,
7. `SESSION_COOKIE_SECURE` - установить в `true` или `false`, если не установлено, то будет установлено в `False`,
8. `CSRF_COOKIE_SECURE` - установить в `true` или `false`, если не установлено, то будет установлено в `False`.

Другие настройки смотрите в [документации](https://docs.djangoproject.com/en/4.2/ref/settings/).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
