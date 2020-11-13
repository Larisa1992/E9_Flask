# E9_Flask Login

Скачать репозиторий на компьютер. Перейти в папку с проектом, открыть командную строку и создать виртуальной окружение командой python -m venv <полный путь до папки> <название окружения>

Активировать окружение: <название окружения>\Scripts\activate.bat

Установить зависимости: pip install -r requirements.txt

Запустить еще одну консоль в корневой папке проекта, где лежит файл docker-compose.yaml проекта. Запустить сборку контейнера docker-compose up --build

Приложение доступно по пути: http://127.0.0.1:5000/

http://127.0.0.1:5000/ - стартовая страница, на которой расположены ссылки для регистрации пользователя, входа-выхода, просмотра и создания событий

http://127.0.0.1:5000/create_user путь для создания пользователя

http://127.0.0.1:5000/login - путь для входа существующего пользователя http://127.0.0.1:5000/logout - разлогинится

http://127.0.0.1:5000/add_event - для залогиненного пользователя доступно создание событий

http://127.0.0.1:5000/events_list - просмотр всех событий только для залогиненнного пользователя В колонке "actions" доступна кнопка для событий, созданных текущим пользователем

При нажатии на кнопку, по пути http://127.0.0.1:5000//events/int:_id/edit открывается форма редактирования события с двумя кнопка "Редактировать", "Удалить".

При нажатии на кнопку "Редактировать" открывается форма редактирования события. Обновления сохраняются при нажатии на кнопку "Обновить"

При нажатии на кнопку "Удалить", событие удаляется и пользователь переадресовывается на страницу со списком всех событий

Приложение развернуто на heroku по ссылке
https://polar-plateau-87337.herokuapp.com/
