<a name="tree"></a>
# Оглавление
* [О проекте](#about)
    * [Распределение ролей в команде](#step-prog)
    * [Описание проекта](#about-proj)
* [Запуск проекта](#start)

<a name="about"></a>
# О проекте

<a name="step-prog"></a>
## Распределение ролей в команде

В разработке данного проекта принимала участие команда студентов Яндекс Практикума. Я отвечал за приложение Users и разрабатывал следующий функционал: *систему регистрации и аутентификации, права доступа, работу с токеном, систему подтверждения через e-mail.*

Мои тиммейты - Александр и Диана - разделили между собой разработку следюущего функционала: категории (Categories), жанры (Genres) и произведения (Titles) - описание моделий, представлений и эндпойнтов для них; отзываы (Review) и комментарии (Comments)- описание модели, представления, настройка эндпойнтов, определение права доступа для запросов и рейтинги произведений.

<a name="about-proj"></a>
## Описание проекта

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

##### ([Вернуться к оглавлению](#tree))

<a name="start"></a>
# Запуск проекта 

1. Склонируйте данный репозиторий

```
git clone https://github.com/CodeWormD/api_yamdb.git
```

2. Перейдите в директорию api_yamdb/. Создайте и активируйте виртуальное окружение. Обновите pip.

```
cd api_yamdb/
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
```

3. Установите зависимости

```
pip install -r requirements.txt
```

3. Выполните миграции

```
python manage.py makemigrations
./manage.py migrate
```

4. Запустите сервер

```
python manage.py runserver
```

5. Если все сделано правильно, то в терминале появится следующее сообщение

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 08, 2022 - 11:12:23
Django version 2.2.16, using settings 'api_yamdb.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

6. Документация API находится по следующему адресу

```
http://127.0.0.1:8000/redoc/
```

##### ([Вернуться к оглавлению](#tree))