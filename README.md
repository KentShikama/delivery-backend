1. git clone
2. virtualenv -p $(which python3) -q ve/
3. source ve/bin/activate
4. pip3 install -r requirements.txt

Useful commands

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
