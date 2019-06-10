# "FROM" starts us out from this Ubuntu-based image
# https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/python3.7/Dockerfile

FROM tiangolo/uwsgi-nginx-flask:python3.7

# Optionally, install some typical packages used for building and network debugging.
RUN apt-get update
RUN apt-get install -y build-essential \
		               software-properties-common \
		               apt-transport-https \
		               build-essential \
		               ca-certificates \
		               checkinstall \
                       netcat \
                       iputils-ping

# Update to the latest PIP
RUN pip3 install --upgrade pip

# Uncommenting this will make rebuilding the image a little faster
# RUN pip3 install Flask==1.0.2 \
#                 flask-inputs==0.3.0 \
#                 jsonschema==3.0.1 \
#                 pytest==4.6.2

# Our application code will exist in the /app directory,
# so set the current working directory to that
WORKDIR /app

# Backup the default app files.  You could also delete these
RUN mkdir bak && \
    mv main.py uwsgi.ini bak


# Copy our files into the current working directory WORKDIR
COPY ./ ./

# install our dependencies
RUN  pip3 install -r requirements.txt

# Make /app/* available to be imported by Python globally to better support several
# use cases like Alembic migrations.
ENV PYTHONPATH=/app
