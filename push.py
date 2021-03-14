import os
import datetime


def run_this(time_1):
    os.system('git add *')
    os.system(f"git commit -m '{time_1[5:10]}'")
    os.system('git push origin master')


time_1 = str(datetime.datetime.now())
run_this(time_1)
