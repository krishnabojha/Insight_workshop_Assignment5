# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:31:12 2020

@author: dell
"""

import keyboard
import os
from Register import Register_info

#print(main.inquiry_obj)


class read_syllabus:
    
    def register(self,fee,course):
        conform=input('Are you trying to register this course? y/n:')
        if conform=='y':
            print('you are ready to register.')
            Register_info().registration(fee,course)
            return
        
        
    def back(self):
        print('Back function is called')
        
    
    def controller(self,course):
        total_fee=20000
        os.system('cls')
        print(5*' '+'Course Detail : ')
        file= open('course_detail/'+course+'.txt','r')
        print(5*' '+file.read())
        file.close()
        print(5*' '+'\nThe Total fee of this course : ',total_fee)
        print('\n'*5)
        print(5*' '+'(NOTE: Press right arrow to register the course. press left arrow key to go back)\n')
        
        while True:
            if keyboard.is_pressed('left'):
                read_syllabus().back()
                break
                
            if keyboard.is_pressed('right'):
                read_syllabus().register(total_fee,course)
        

