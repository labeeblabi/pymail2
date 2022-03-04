FROM ubuntu:18.04
RUN apt update
RUN apt upgrade -y
RUN touch /var/log/cron.log
ADD PyMail-MailJet.py /PyMail-MailJet.py
RUN chmod 0644 /PyMail-MailJet.py
RUN apt-get -y install cron
RUN apt-get install -y python python-pip
RUN pip install mailjet-rest==1.3.4
RUN crontab -l | { cat; echo "*/2 * * * * /usr/bin/python PyMail-MailJet.py"; } | crontab -
CMD cron && tail -f  /var/log/cron.log
