# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:05:35 2020

@author: dell
"""

import os
import csv
global random_fee
random_fee=False
class Register_info:
    
    def save(self, info, header):
   #     print(info)
        file=open('student_detail.txt','a')
        filewriter=csv.DictWriter(file,fieldnames=header)
     #   filewriter.writeheader()
        filewriter.writerows(info)
        file.close()
        print('You are Registered for this course.\n Ready to Learn !!!\n')
        print('\nPress left arrow key to return HOME PAGE')
        return
        
    def registration(self,total_fee,course):
        global random_fee
        os.system('cls')
        if random_fee==True:
            print('You must deposit atleast half of the course fee.i.e {}'.format(total_fee/2))
        info=[{}]
        header=['Name','Email','Address','Education','Deposit amount','Voucher number']
        print('\nREGISTRATION FORM')
        for i in header:
            info[0][i]=input(i+' : ')
        
        header.append('Payment')
        header.append('Course')
        info[0]['Course']=course
        if total_fee/2==int(info[0]['Deposit amount']):
            info[0]['Payment']='installment'
            Register_info().save(info, header)
            return
        elif total_fee==int(info[0]['Deposit amount']):
            info[0]['Payment']='paid'
            Register_info().save(info, header)
            return
        else:
            os.system('cls')
            random_fee=True
            Register_info().registration(total_fee)
        
#obj=Register_info()
#obj.registration(20000)