FROM ubuntu:18.04
RUN apt update
RUN apt upgrade -y
ADD crontab /etc/cron.d/hello-cron
RUN chmod 0644 /etc/cron.d/hello-cron
RUN  apt install cron -y
COPY PyMail-MailJet.py /home/python/
RUN chmod +x /home/python/PyMail-MailJet.py
RUN apt-get install -y python python-pip
RUN pip install mailjet-rest==1.3.4
CMD cron 
