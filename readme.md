1) you need to create virtual env by command :- python -m env venv
2) activate virtual env:- source venv/bin/activate (according to your directory path) 
3) install requirements.txt file :- python manage.py -r requirements.txt
4) run make migrations and migrate :- python manage.py makemigrations , python manage.py migrate 
5) make superuser :- python manage.py createsuperuser 
6) then run server :- python manage.py runserver 
7) scrapping will be start and it will take time to scrap then it will be seen into csv_file and data will be saved into db .
