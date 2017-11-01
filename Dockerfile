
FROM python:3.6
VOLUME  /tmp
COPY .   /mysite

WORKDIR /mysite
#RUN pip3 install -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

EXPOSE 8000
ENTRYPOINT [ "sh", "-c", "python3 manage.py runserver 0.0.0.0:8000" ]