# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:54:13 2019

@author: Veena Chintala
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('C:/Users/Veena Chintala/Desktop/326/football/FullData.csv')

del df['National_Kit']

ntnCount = df['Nationality'].value_counts().reset_index().head(30)
ntnCount.columns = ['Nationality','frequency_count']
plt.figure(figsize=(15,32))
sns.barplot(x=ntnCount['Nationality'],y=ntnCount['frequency_count'])
plt.xticks(rotation ='vertical')
plt.show()

#Most of the players are from England,Argentina,Spain,France and Brazil

plt.figure(figsize=(12,7))
sns.countplot(x=df['Age'])
# Most players are between the age 20 and 29 with peak of 25 years

#Finding the best Goal Keeper

#weights
a = 0.5
b = 1
c= 2
d = 3
 
#GoalKeeping Characterstics
df['gk_Shot_Stopper'] = (b*df.Reactions + b*df.Composure + a*df.Speed + 
  a*df.Strength + c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving +
  d*df.GK_Reflexes + b*df.GK_Handling)/(2*a + 4*b + 2*c + 1*d)
df['gk_Sweeper'] = (b*df.Reactions + b*df.Composure + b*df.Speed + 
  a*df.Short_Pass + a*df.Long_Pass + b*df.Jumping + b*df.GK_Positioning 
  + b*df.GK_Diving + d*df.GK_Reflexes + b*df.GK_Handling + d*df.GK_Kicking +
  c*df.Vision)/(2*a + 4*b + 3*c + 2*d)

#best_Shot_Stoper = df['gk_Shot_Stopper'].sort_values(ascending = False).head(5)
sd = df.sort_values('gk_Shot_Stopper', ascending=False)[:5]
x=np.array(list(sd['Name']))
y=np.array(list(sd['gk_Shot_Stopper']))
plt.figure()
sns.barplot(x,y)
plt.xticks(rotation='vertical')
plt.show()
#Manuel Neuer is the best goal keeper

bstSweepr = df.sort_values('gk_Sweeper',ascending=False).head(5)
xx=np.array(list(bstSweepr['Name']))
yy=np.array(list(bstSweepr['gk_Sweeper']))
plt.figure()
sns.barplot(xx,yy)
plt.xticks(rotation='vertical')
plt.show()
#Manuel Neuer is the best goal keeper

#Choosing Defenders
df['df_centre_backs'] = ( d*df.Reactions + c*df.Interceptions + d*df.Sliding_Tackle + d*df.Standing_Tackle + b*df.Vision+ b*df.Composure + b*df.Crossing +a*df.Short_Pass + b*df.Long_Pass+ c*df.Acceleration + b*df.Speed
+ d*df.Stamina + d*df.Jumping + d*df.Heading + b*df.Long_Shots + d*df.Marking + c*df.Aggression)/(6*b + 3*c + 7*d)
df['df_wb_Wing_Backs'] = (b*df.Ball_Control + a*df.Dribbling + a*df.Marking + d*df.Sliding_Tackle + d*df.Standing_Tackle + a*df.Attacking_Position + c*df.Vision + c*df.Crossing + b*df.Short_Pass + c*df.Long_Pass + d*df.Acceleration +d*df.Speed + c*df.Stamina + a*df.Finishing)/(4*a + 2*b + 4*c + 4*d)



























