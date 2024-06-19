### README.md

# Автообъявления / Car Advertisements

Этот проект представляет собой веб-приложение для размещения объявлений о продаже автомобилей. Приложение поддерживает регистрацию, авторизацию пользователей, создание и просмотр объявлений, а также другие функции.  
This project is a web application for posting car sale advertisements. The application supports user registration, authentication, creation and viewing of advertisements, and other features.

## Структура проекта / Project Structure

Проект состоит из следующих основных файлов:  
The project consists of the following main files:

### Бэкенд / Backend

1. **urls.py**: Содержит маршруты (URL) для API.  
   **urls.py**: Contains routes (URLs) for the API.
2. **views.py**: Определяет представления для обработки запросов.  
   **views.py**: Defines views for handling requests.
3. **models.py**: Содержит модели базы данных.  
   **models.py**: Contains database models.
4. **pagination.py**: Реализует логику пагинации для вывода объявлений.  
   **pagination.py**: Implements pagination logic for listing advertisements.
5. **send_tg_messages.py**: Модуль для отправки сообщений в Telegram.  
   **send_tg_messages.py**: Module for sending messages to Telegram.
6. **serializers.py**: Содержит сериализаторы для преобразования данных моделей в JSON и обратно.  
   **serializers.py**: Contains serializers for converting model data to and from JSON.
7. **db_transfer.py**: Модуль для переноса данных между различными базами данных.  
   **db_transfer.py**: Module for transferring data between different databases.

### Фронтенд / Frontend

1. **App.js**: Основной файл фронтенда, написанный на React.  
   **App.js**: Main frontend file written in React.
2. **Auto_z_prob_detail.jsx**: Компонент для отображения детальной информации об автомобиле с пробегом.  
   **Auto_z_prob_detail.jsx**: Component for displaying detailed information about a used car.
3. **Auto_z_probegom.jsx**: Компонент для отображения списка автомобилей с пробегом.  
   **Auto_z_probegom.jsx**: Component for displaying a list of used cars.
4. **CarAdvertCreate.jsx**: Компонент для создания нового объявления.  
   **CarAdvertCreate.jsx**: Component for creating a new advertisement.
5. **CarAdvertDetail.jsx**: Компонент для отображения детальной информации об объявлении.  
   **CarAdvertDetail.jsx**: Component for displaying detailed information about an advertisement.
6. **CarAdvertList.jsx**: Компонент для отображения списка объявлений пользователя.  
   **CarAdvertList.jsx**: Component for displaying the list of user's advertisements.
7. **CarDetail.jsx**: Компонент для отображения детальной информации об автомобиле.  
   **CarDetail.jsx**: Component for displaying detailed information about a car.
8. **CarList.jsx**: Компонент для отображения списка автомобилей.  
   **CarList.jsx**: Component for displaying the list of cars.

## Установка и настройка / Installation and Setup

### Требования / Requirements

- Python 3.x
- Django
- Django REST Framework
- Node.js
- React.js

### Установка / Installation

1. Клонируйте репозиторий:  
   Clone the repository:
   ```bash
   git clone [<URL репозитория>]
   git clone <repository URL>
   ```

2. Перейдите в директорию проекта:  
   Navigate to the project directory:
   ```bash
   cd <название директории>
   cd <directory name>
   ```

3. Установите зависимости для бэкенда:  
   Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Настройте базу данных и примените миграции:  
   Set up the database and apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Запустите сервер разработки Django:  
   Run the Django development server:
   ```bash
   python manage.py runserver
   ```

6. Перейдите в директорию фронтенда и установите зависимости:  
   Navigate to the frontend directory and install dependencies:
   ```bash
   cd frontend
   npm install
   ```

7. Запустите сервер разработки React:  
   Run the React development server:
   ```bash
   npm start
   ```

## Основные компоненты / Main Components

### urls.py

Содержит маршруты для API, включая маршруты для работы с объявлениями о продаже автомобилей, аутентификации и другие.  
Contains routes for the API, including routes for handling car sale advertisements, authentication, and others.

### views.py

Определяет представления для обработки запросов. Например, создание, редактирование и удаление объявлений.  
Defines views for handling requests. For example, creating, editing, and deleting advertisements.

### models.py

Содержит модели базы данных, такие как модель для хранения информации об автомобилях.  
Contains database models, such as the model for storing car information.

### pagination.py

Реализует логику пагинации для вывода большого количества объявлений.  
Implements pagination logic for listing a large number of advertisements.

### send_tg_messages.py

Модуль для отправки уведомлений в Telegram.  
Module for sending notifications to Telegram.

### serializers.py

Содержит сериализаторы для преобразования данных моделей в JSON и обратно, что необходимо для работы с API.  
Contains serializers for converting model data to and from JSON, necessary for API functionality.

### db_transfer.py

Модуль для переноса данных между различными базами данных.  
Module for transferring data between different databases.

### App.js

Основной файл фронтенда, написанный на React. Управляет маршрутизацией и отображением компонентов.  
Main frontend file written in React. Manages routing and component rendering.

#### Компоненты / Components

- **CarList**: Список автомобилей.  
  **CarList**: List of cars.
- **CarDetail**: Детальная информация о выбранном автомобиле.  
  **CarDetail**: Detailed information about a selected car.
- **CarAdvertCreate**: Создание нового объявления.  
  **CarAdvertCreate**: Creating a new advertisement.
- **CarAdvertList**: Список объявлений пользователя.  
  **CarAdvertList**: List of user's advertisements.
- **CarAdvertDetail**: Детальная информация об объявлении.  
  **CarAdvertDetail**: Detailed information about an advertisement.
- **AuthComponent**: Компонент для авторизации.  
  **AuthComponent**: Component for authentication.
- **LogOutComponent**: Компонент для выхода из аккаунта.  
  **LogOutComponent**: Component for logging out.
- **Auto_z_probegom**: Список автомобилей с пробегом.  
  **Auto_z_probegom**: List of used cars.
- **Auto_z_prob_detail**: Детальная информация об автомобиле с пробегом.  
  **Auto_z_prob_detail**: Detailed information about a used car.

## Примеры использования / Usage Examples

### Пример создания объявления / Example of Creating an Advertisement

1. Перейдите на страницу создания объявления.  
   Navigate to the advertisement creation page.
2. Заполните форму с информацией об автомобиле.  
   Fill out the form with car information.
3. Нажмите "Подать объявление".  
   Click "Submit Advertisement".

### Пример просмотра списка объявлений / Example of Viewing Advertisement List

1. Перейдите на страницу списка объявлений.  
   Navigate to the advertisement list page.
2. Выберите интересующее объявление для просмотра детальной информации.  
   Select the advertisement you are interested in to view detailed information.

## Контакты / Contacts

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по email: victoria.grib@gmail.com  
If you have any questions or suggestions, please contact us at: victoria.grib@gmail.com
```


