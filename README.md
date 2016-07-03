
#Wasman


To deploy this project follow the following steps

```sudo apt-get install python-pip python-dev libmysqlclient-dev binutils libproj-dev gdal-bin git```

**Setup the database**
```
create user 'wasman' identified by 'wasman';
create database 'wasman';
grant all privileges on wasman.* to wasman;
```

**Setup virtual environment**
```
sudo pip install virtualenv
sudo pip install virtualenvwrapper
mkdir -p /home/$usr/.Envs/
export WORKON_HOME=/home/$use/.Envs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv wasman
```

**Add the following lines to ~/.bashrc**
```
export WORKON_HOME=/home/$use/.Envs
source /usr/local/bin/virtualenvwrapper.sh
```
 
**Setup the project**
```
git clone git@github.com:lekhajk/wasman.git
workon wasman
pip install -r requirements.txt
python manage.py migrate
./manage.py cities --force --import=all
```

**To start the django server**

`python manage.py runserver` for local acccess on localhost:8000

`python manage.py runserver 0.0.0.0:8000` fot internal and external access
