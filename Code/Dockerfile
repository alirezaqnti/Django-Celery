FROM python:3.11.4-alpine
# first we need an image.
# images are like a blueprint of everything that needed to run our apllications
# this is pre-created Docker Image which has a copy of Alpine (Alpine Linux)
# A lightweight and minimalistic linux distribution that is very commonly used as a based image for Docker containers 

WORKDIR /usr/src/app/

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED=1

# to get the latest version of pip
RUN pip install --upgrade pip

# copy the requirements file and install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# entrypoint runs everytime that container runs
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]