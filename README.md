# Автообъявления / Car Advertisements

Этот проект представляет собой веб-приложение для размещения объявлений о продаже автомобилей. Приложение поддерживает регистрацию, авторизацию пользователей, создание и просмотр объявлений, а также другие функции.
This project is a web application for posting car sale advertisements. The application supports user registration, authentication, creation and viewing of advertisements, and other features.

## Структура проекта / Project Structure

Проект состоит из следующих основных файлов:
The project consists of the following main files:

### Бэкенд / Backend

1. **urls.py**: Содержит маршруты (URL) для API.
1. **urls.py**: Contains routes (URLs) for the API.
2. **views.py**: Определяет представления для обработки запросов.
2. **views.py**: Defines views for handling requests.
3. **models.py**: Содержит модели базы данных.
3. **models.py**: Contains database models.
4. **pagination.py**: Реализует логику пагинации для вывода объявлений.
4. **pagination.py**: Implements pagination logic for listing advertisements.
5. **send_tg_messages.py**: Модуль для отправки сообщений в Telegram.
5. **send_tg_messages.py**: Module for sending messages to Telegram.
6. **serializers.py**: Содержит сериализаторы для преобразования данных моделей в JSON и обратно.
6. **serializers.py**: Contains serializers for converting model data to and from JSON.
7. **db_transfer.py**: Модуль для переноса данных между различными базами данных.
7. **db_transfer.py**: Module for transferring data between different databases.

### Фронтенд / Frontend

1. **App.js**: Основной файл фронтенда, написанный на React.
1. **App.js**: Main frontend file written in React.
2. **Auto_z_prob_detail.jsx**: Компонент для отображения детальной информации об автомобиле с пробегом.
2. **Auto_z_prob_detail.jsx**: Component for displaying detailed information about a used car.
3. **Auto_z_probegom.jsx**: Компонент для отображения списка автомобилей с пробегом.
3. **Auto_z_probegom.jsx**: Component for displaying a list of used cars.
4. **CarAdvertCreate.jsx**: Компонент для создания нового объявления.
4. **CarAdvertCreate.jsx**: Component for creating a new advertisement.
5. **CarAdvertDetail.jsx**: Компонент для отображения детальной информации об объявлении.
5. **CarAdvertDetail.jsx**: Component for displaying detailed information about an advertisement.
6. **CarAdvertList.jsx**: Компонент для отображения списка объявлений пользователя.
6. **CarAdvertList.jsx**: Component for displaying the list of user's advertisements.
7. **CarDetail.jsx**: Компонент для отображения детальной информации об автомобиле.
7. **CarDetail.jsx**: Component for displaying detailed information about a car.
8. **CarList.jsx**: Компонент для отображения списка автомобилей.
8. **CarList.jsx**: Component for displaying the list of cars.

## Установка и настройка / Installation and Setup

### Требования / Requirements

- Python 3.x
- Django
- Django REST Framework
- Node.js
- React.js

### Установка / Installation

1. Клонируйте репозиторий:
1. Clone the repository:
   ```bash
   git clone <URL репозитория>
   git clone <repository URL>```

2. Перейдите в директорию проекта:
2. Navigate to the project directory:
 ```cd <название директории>
cd <directory name>```

3. Установите зависимости для бэкенда:
3. Install backend dependencies:
```
pip install -r requirements.txt
```

4. Настройте базу данных и примените миграции:
4. Set up the database and apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```

5. Запустите сервер разработки Django:
5. Run the Django development server:

```
python manage.py runserver
```

6. Перейдите в директорию фронтенда и установите зависимости:
6. Navigate to the frontend directory and install dependencies:
```
cd frontend
npm install
```

7. Запустите сервер разработки React:
7. Run the React development server:
```
npm start
```

### Контакты / Contacts
Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по email: victoria.grib@gmail.com
If you have any questions or suggestions, please contact us at: victoria.grib@gmail.com
