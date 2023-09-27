python -m venv venv
source venv/bin/activate
pip3 install django
pip3 install redis
pip3 install celery
pip3 freeze > requirements.txt
chmod +x/entrypoint.sh
http://0.0.0.0:8000/
docker-compose up -d--build