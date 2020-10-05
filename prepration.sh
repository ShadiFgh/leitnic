#!/bin/bash

sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo python3 manage.py collectstatic

sudo chown www-data db.sqlite3
sudo chown www-data .
chmod 664 db.sqlite3

sudo chown :www-data db.sqlite3
sudo chown :www-data .

sudo chmod -R 777 /var/www/
sudo chmod -R 777 /var/www/

sudo service apache2 restart
