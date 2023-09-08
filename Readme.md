## Проект напоминания о привычках
____
### Описание
DRF Приложение позволяющее заносить свои привычки, отслеживать их и получать напоминания 
о них через telegram бота.

##### Модели
1. Habit - Модель привычки.
2. User - Кастомная модель пользователей.

##### Валидация
1. Для основной привычки может быть задана либо связанная приятная привычка (related_habit), 
либо вознаграждение поле (reward). Они не могут быть одновременно. Валидация на уровне сериализатора.\
2. У приятной привычки не может быть вознаграждения. Валидация на уровне сериализотора.\
3. Время выполнения привычки должно быть не больше 120 секунд. Валидация через кастомный валидатор.\
4. Нельзя выполнять привычку реже, чем 1 раз в 7 дней. Валидация через кастомный валидатор.\
5. Связанная привычка должна быть приятной. Валидация через кастомный валидатор. 

##### Пагинация
Для вывода списка привычек реализована пагинация с выводом по 5 привычек на страницу

##### Права доступа
Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD. 
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

##### Эндпоинты и документация
Настроена документация yasg-drf. Все эндпоинты можно изучить по ссылкам: 
http://localhost:8000/redoc/ http://localhost:8000/dosc/

##### Безопасность
Для проекта настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере. В данном случае localhost.