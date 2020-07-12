# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 19:49:43 2020

@author: dell
"""

import os
import pandas as pd
import keyboard
import csv
import sys

os.system('cls')

selected=1
option_list=['Delete','Edit','Return Deposit','Exit']

class Arrow_move:
    def show_menu():
        global selected
        print(5*' '+"\nStudent's Detail: \n")
        print(5*' '+"Select Options(use up and down arrow key):\n")
        for i in range(1,5):
            print(5*' '+"{}".format(">" if selected == i else " ")+option_list[i-1]+" {}".format("<" if selected == i else " "))
        
        print(5*' '+'(Note: Use right arrow to select )')
        print('\n')
        print('ID')
        Arrow_move.show_data()
            
    def up():
        global selected
        if selected < 1:
            selected=1
    
        selected -= 1
        if(selected>0):
            os.system('cls')
            Arrow_move.show_menu()
    
    def down():
        global selected
        if selected > 5:
            selected=5
        selected += 1
        if(selected<5):
            os.system('cls')
            Arrow_move.show_menu()
    
    def show_data():
        data=pd.read_csv('student_detail.txt')
        print(data[:][:])
class Play_With_Data(Arrow_move): 
    
    def delete():
        username=''
        #1. This code snippet asks the user for a username and deletes the user's record from file.
        updatedlist=[]
        student_name=[]
        with open("student_detail.txt",newline="") as f:
          reader=csv.reader(f)
          
          print('\n')
          print("(NOTE: type exit to go BACK.)")
          username=input("Enter the Name of the student you want to delete from file:")
          if username=='exit':
              return 'delete'
          
          for row in reader: #for every row in the file
                student_name.append(row[0])
                print(student_name)
                if row[0]!=username: #as long as the username is not in the row .......
                    updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
    #       print('This is',updatedlist)
            
          
          delete_info='Info of {} has been deleted.'.format(username)
          Play_With_Data.updatefile(updatedlist)
          print(delete_info)
          if username not in student_name:
            os.system('cls')
            username=''
            Arrow_move.show_menu()
            Play_With_Data.delete()
            
           
          
    def updatefile(updatedlist):
        with open("student_detail.txt","w",newline="") as f:
            os.system('cls')
            Writer=csv.writer(f)
            Writer.writerows(updatedlist)
            Play_With_Data.controller()
            
            #print("File has been Updated")
            
    def edit_info(s_id,head,new_data):
        data=pd.read_csv('student_detail.txt')
        df=pd.DataFrame(data)
        df[:][s_id:(s_id+1)][head]=new_data
        df.to_csv(r'student_detail.txt',index=False)
        os.system('cls')
        print('Your updated {} has saved.'.format(head))
        Arrow_move.show_menu()
        
    def selected_option():
        try:
            if option_list[selected-1]=='Delete':
                print('\n\nyou selected  : ',option_list[selected-1])
                Play_With_Data.delete()
                
            elif option_list[selected-1]=='Edit':
                s_id=int(input('Enter ID of the Student : '))
                head=input('Enter a header name of data you want to update : ')
                head=head[0].upper()+head[1:]
                print(head)
                new_data=input('Type a new {} : '.format(head))
             #   print(df[:][s_id:(s_id+1)])
                Play_With_Data.edit_info(s_id,head,new_data)
            
            elif option_list[selected-1]=='Return Deposit':
                s_id=int(input('Enter ID of the Student : '))
                Play_With_Data.edit_info(s_id, 'Payment', 'Deposit returned')
            
            elif option_list[selected-1]=='Exit':
                return 'exit_true'
        except:
            os.system('cls')
            Arrow_move.show_menu()
            Play_With_Data.selected_option()
        
    def controller():
        abc='start'
        Arrow_move.show_menu()
        while True:
            
            if keyboard.is_pressed('up'):
                Arrow_move.up()
                
                
            if keyboard.is_pressed('down'):
                Arrow_move.down()
                
                
            if keyboard.is_pressed('right'):
                abc=Play_With_Data.selected_option()
                if abc=='delete':
                    break
            if abc=='exit_true':
                return True
       # Arrow_move.keyboard.add_hotkey('up', up)
       # Arrow_move.keyboard.add_hotkey('down', down)
       # Arrow_move.keyboard.add_hotkey('right', selected_option)
       # Arrow_move.keyboard.wait()
        
    
#Play_With_Data.controller()