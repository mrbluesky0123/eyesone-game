FROM python:3
# RUN add-apt-repository ppa:jonathonf/python-3.6
# RUN apt-get install -y --fix-missing build-essential
RUN apt-get --fix-missing update 
# RUN apt-get install --fix-missing -y python3-pip
# RUN ln -s /usr/bin/python3 /usr/bin/python
# RUN ln -s /usr/bin/pip3 /usr/bin/pip
# RUN pip install --upgrade pip
WORKDIR /home/root/
RUN apt-get install -y python3-mysqldb libmariadb-dev
RUN mkdir /code 
WORKDIR /code
ADD requirements.txt /code 
EXPOSE 5000
RUN pip install -r requirements.txt
ADD . /code
ENV SERVER_PORT 5000
RUN pytest
CMD python app.py $SERVER_PORT