# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:19:43 2020

@author: dell
"""


import keyboard
import os
import pandas as pd
from inquiry import read_syllabus
from Admin import Play_With_Data

space=" "
selected = 1
os.system('cls')

course_data=pd.read_csv('course.csv')
num_courses=len(course_data)
def show_menu():
    global selected
    print('\n'*2)
    print(5*space+'COURSES'+15*space+'Admin(A)')
    print('\n'*3)
    print(5*space+"Courses we provide:\n")
    for i in range(1,num_courses):
        print(5*space+"{}".format(">" if selected == i else " ")+course_data['courses'][i]+" {}".format("<" if selected == i else " "))
        
    print('\n'*5)
    print('(NOTE : press LEFT arrow key to go back and RIGHT arrow key to go forward(SELECT).\n press A to go ADMIN PANNEL)')
        
def up():
    global selected
    if selected < 1:
        selected=1

    selected -= 1
    if(selected>0):
        os.system('cls')
        show_menu()

def down():
    global selected
    if selected > num_courses:
        selected=num_courses
    selected += 1
    if(selected<num_courses):
        os.system('cls')
        show_menu()
    
def select_course():
    print('you selected a course',course_data['courses'][selected])
    #read_syllabus().get_data(course=course_data['courses'][selected])
    
    read_syllabus().controller(course_data['courses'][selected])
    
    os.system('cls')

    show_menu()

#def portfolio():
 #   print('portfolio call')

def admin():
#    print('admin call')
    os.system('cls')
    Play_With_Data.controller()
    os.system('cls')
#    print('Home page')
    show_menu() 


show_menu()
#inquiry_obj=read_syllabus()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', select_course)
if keyboard.is_pressed('shift+a'):
    admin()
keyboard.add_hotkey('shift+a', admin)
#keyboard.add_hotkey('shift+p', portfolio)
keyboard.wait()



