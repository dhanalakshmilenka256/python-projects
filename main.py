
'''my_email="dhanalakshmilenka256@gmail.com"
password="nlqmoxdtllahzfwk"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="dhanaskgd@gmail.com",msg="subject:Hello\n\nThis is the body of the email")

import smtplib
import datetime as dt
import random
my_email="dhanalakshmilenka256@gmail.com"
my_password="dhanalaxmi"

now=dt.datetime.now()
#year=now.year
#month=now.month
#date_of_birth=dt.datetime(year=2002,month=12,day=1,hour=4)
#print(date_of_birth)
Weekday=now.weekday()
if Weekday==1:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}")'''
import datetime as dt
import pandas
import smtplib
my_email="dhanalakshmilenka256@gmail.com"
my_password="nlqmoxdtllahzfwk"
#today=(dt.datetime.now().month,dt.datetime.now().day)
today=dt.datetime.now()
today_tuple=(today.month,today.day)

data=pandas.read_csv("birtdays.csv")
birthday_dict={(data_row.month,data_row.day):data_row for(index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path="letter.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")
















