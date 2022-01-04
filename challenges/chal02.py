#/usr/bin/env python3
import random
import datetime
icecream = ["indentation", "spaces"]
tlgstudents= ["Aaron","Alex","Alonzo","Brandon","Chris","Francisco","James","Jonathan","Lillian","Manuel","Patrick","Robert","Ryan","Troy","Wes","Henry","Yalined"]
icecream.append(4)
student = input("To pick a student enter their name or a number between 0 and 16,\n for random selection, enter 17: ")

if int(student) >= 0 and int(student) <= 16:
    print(f"{tlgstudents[int(student)]} always uses {icecream[2]} {icecream[1]} to {icecream[0][0:6]}.")
elif int(student) == 17:
    random.seed(datetime.datetime.now())
    rand_select = random.randint(0,16)
    print(f"{tlgstudents[rand_select]} always uses {icecream[2]} {icecream[1]} to {icecream[0][0:6]}.")
else:
    print("Wrong selection, please try again later")
