from datetime import *
import os
import ctypes

print (datetime.today().day)

ctypes.windll.user32.MessageBoxW(0, u"An unexpected error occured. Reporting problem", u"Unexpected Error", 0)

filelog = open(f'/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/log.txt', 'a+')

#bro = os.getcwd()

# os.makedirs(f'{bro}/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/')