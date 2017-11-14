# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 17:06:45 2016

@author: PHAM MinhQuang
"""

from numpy import *
import pandas as pd
import datetime
import csv
from sklearn import linear_model
from sklearn.decomposition import PCA

#category function
def assignment(x):
    return{
        'CAT': 0,
        'CMS': 1,
        'Crises': 2,
        'Domicile': 3,
        'Gestion': 4,
        'Gestion - Accueil Telephonique': 5,
        'Gestion Amex': 6,
        'Gestion Assurances': 7,
        'Gestion Clients': 8,
        'Gestion DZ': 9,
        'Gestion Relation Clienteles': 10,
        'Gestion Renault': 11,
        'Japon': 12,
        'Manager': 13,
        'Mécanicien': 14,
        'Médical': 15,
        'Nuit': 16,
        'Prestataires': 17,
        'RENAULT': 18,
        'RTC': 19,
        'Regulation Medicale': 20,
        'SAP': 21,
        'Services': 22,
        'Tech. Axa': 23,
        'Tech. Inter': 24,
        'Tech. Total': 25,
        'Téléphonie': 26,
        'Evenements':27
    }[x]
    
list_holidays = [datetime.date(2013, 1, 1),datetime.date(2013, 4, 1),datetime.date(2013, 5, 1),datetime.date(2013, 5, 8),
datetime.date(2013, 5, 9),datetime.date(2013, 5, 20),datetime.date(2013, 5, 30),datetime.date(2013, 7, 14),datetime.date(2013, 8, 15),datetime.date(2013, 11, 1),datetime.date(2013, 11, 11),datetime.date(2013, 12, 25),
datetime.date(2012, 1, 1),datetime.date(2012, 4, 1),datetime.date(2012, 5, 1),datetime.date(2012, 5, 8),
datetime.date(2012, 5, 9),datetime.date(2012, 5, 20),datetime.date(2012, 5, 30),datetime.date(2012, 7, 14),
datetime.date(2012, 8, 15),datetime.date(2012, 11, 1),datetime.date(2012, 11, 11),datetime.date(2012, 12, 25)]

#load file submission.txt to predict and buid the submission file
f=open("submission2.txt",'w')
ff = open("results.txt", 'r')
lines = ff.readlines()
q = 0

f.write('DATE\tASS_ASSIGNMENT\tprediction\n')
iter=0
pred=[]
with open("submission.txt", 'rb') as csvfile:
    reader =csv.DictReader(csvfile,delimiter='\t')
    for row in reader:
        date=str(row['DATE'])
        tmp_list = row['DATE'].split(' ')
        date_list = tmp_list[0].split('-')
        time_list = tmp_list[1].split(':')
        current_day = datetime.date(int(date_list[0]),int(date_list[1]),int(date_list[2]))
        current_time = datetime.datetime(int(date_list[0]),int(date_list[1]),int(date_list[2]),int(time_list[0]),int(time_list[1]))
        day = datetime.datetime(int(date_list[0]),int(date_list[1]),int(date_list[2]),7,30,0)
        night = datetime.datetime(int(date_list[0]),int(date_list[1]),int(date_list[2]),23,30,0)
        x=zeros(11)
        x[0] = int(date_list[0]) #year from 2011
        x[1] = int(date_list[1]) #month
        x[2] = int(date_list[2]) #day
        x[3] = int(time_list[0])
        x[4] = int(time_list[1])
        x[5] = int(time_list[0])*2 + int(time_list[1])/30
        x[6] = int(time_list[0])
        if((current_time.time()>day.time()) and (current_time.time()<night.time())):
            x[7] = 1
        else: x[7] = 0
        x[8]=current_time.weekday()+1
        if(x[8]==6 or x[8]==7):
            x[9]=1
        else: x[9]=0
        x[10] = int(current_day in list_holidays)
        
        assign=str(row['ASS_ASSIGNMENT'])
        cat=assignment(str(row['ASS_ASSIGNMENT']))
        print cat
        
        f.write(date+'\t')
        f.write(assign+'\t')
        line = ff.read()
        f.write(lines[q])
        q += 1
                
        iter=iter+1
        print iter

ff.close()
f.close() 
