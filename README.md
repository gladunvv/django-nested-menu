# nested-menu
Tree menu in Django           


## Приложение для отрисовки меню с помощью templatetag

### Содержание:
+ [Краткое описание](#краткое-описание)
+ [Полезные ссылки](#полезные-ссылки)
+ [Requirements](#requirements)
+ [Сборка и запуск проекта](#сборка-и-запуск)        




### Краткое описание:
Простое Django приложение для отрисовки древовидного меню, реализованное через templatetag. Меню и его элементы создаются и редактируются в админ панели Django. С помощью тега {% draw_menu 'menu_name' %} меню можно расположить на любой странице приложения.




### Полезные ссылки:
+ [Django documentation](https://docs.djangoproject.com/en/2.2/)         



### Requirements:
+ Django==2.2.7
+ pytz==2019.3
+ sqlparse==0.3.0       




### Сборка и запуск:
! Для корректного отображения меню при запуске следует сначала создать его а так-же добавить в него элементы в админ панели Django.
```bash
git clone git@github.com:gladunvv/django-nested-menu.git
cd django-nested-menu
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd nested_menu/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### License
This project is licensed under the terms of the MIT license