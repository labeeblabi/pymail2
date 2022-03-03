from datetime import datetime
from mailjet_rest import Client


def main_function():
    time_calc()


def time_calc():
    try:
        current_date_time = datetime.now()
        date_object = current_date_time.strftime("%d/%m/%Y")
        time_object = current_date_time.strftime("%H:%M:%S")

        send_mail(date_object, time_object)
    except Exception as e:
        fatal_error('Exception caught while calculating current time:'+e)
    print()


def send_mail(date_object, time_object):
    try:
        api_key = '7f28e3962221015dbfe7d25d3978f051'
        api_secret = '78921b11683df98eaec2be8a4cfb95db'
        mail_recepients = ['206551@ust-global.com']  # - PROVIDE MAIL ID OF RECEPIENTS HERE (COMMA SEPERATED) 

        for recepients in mail_recepients:
            mailjet = Client(auth=(api_key, api_secret), version='v3.1')
            data = {
              'Messages': [
                {
                  "From": {
                    "Email": "python.noreply.500@gmail.com",
                    "Name": "no-reply@python.com"
                  },
                  "To": [
                    {
                      "Email": recepients,
                      "Name": "Py"
                    }
                  ],
                  "Subject": "Test Mail From Python-Container",
                  "TextPart": "Test Mail From Python-Container",
                  "HTMLPart": "Hi There! \n \nThis is an auto generated test mail sent using Python-Docker Container. \n \nPlease Ignore. \n \nTrigger Time:" + date_object + " at " + time_object,
                  "CustomID": "AppGettingStartedTest"
                }
              ]
            }
            result = mailjet.send.create(data=data)
            print (result.status_code)
            print (result.json())
    except Exception as e:
        fatal_error('Exception caught while sending mail using REST API:'+e)
    print()



def fatal_error(message):
    print('\033[31mERROR: ' + message + '\033[0m')
    exit


if __name__ == "__main__":
    main_function()