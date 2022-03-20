# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello world!")
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

result=np.loadtxt("datasets/cumulative_cases.csv",skiprows=1,usecols=(4),unpack=True,delimiter=',')
result_1=result[::-1]
result_2=np.loadtxt("datasets/vaccination_first_dose.csv",skiprows=1,usecols=4,unpack=True,delimiter=',')
result_3=result_2[::-1]
result_4=np.loadtxt("datasets/vaccination_second_dose.csv",skiprows=1,usecols=4,unpack=True,delimiter=',')
result_5=result_4[::-1]
daily_cases=[]
daily_vaccination_1=[]
daily_vaccination_2=[]

for i in range(len(result_1)-1):
    daily_cases.append(result_1[i+1]-result_1[i])
for i in range(len(result_3)-1):
    daily_vaccination_1.append(result_3[i+1]-result_3[i])
for i in range(len(result_5)-1):
    daily_vaccination_2.append(result_5[i+1]-result_5[i])
# print(daily_cases)
date_1=np.arange(0,len(daily_cases))
date_2=np.arange(len(daily_cases)-len(daily_vaccination_1),len(daily_cases))
date_3=np.arange(len(daily_cases)-len(daily_vaccination_2),len(daily_cases))
plt.plot(date_1,daily_cases)
plt.plot(date_2,daily_vaccination_1)
plt.plot(date_3,daily_vaccination_2)
plt.title('vaccination and infection plot')
plt.ylabel('number of people')
plt.xlabel('number of days since the pandemic')
plt.legend(['daily cases','first dose','second dose'])
plt.show()
#%%
vaccination_by_age=np.loadtxt("datasets/vaccination_by_age_group.csv",skiprows=1,usecols=(7),unpack=True,delimiter=',')
vaccination_12_17=[] #everyday number of people vaccinated between 12 and 17
for i in range(0,442):#There are 442 days in total
    vaccination_12_17.append(vaccination_by_age[17*i]+vaccination_by_age[17*i+1])   
vaccination_12_17=vaccination_12_17[::-1] #reverse the list
vaccination_18_64=[] #everyday number of people vaccinated between 18 and 64
for i in range(0,442):
    vaccination_18_64.append(vaccination_by_age[17*i+2]+vaccination_by_age[17*i+3]+vaccination_by_age[17*i+4]+\
                vaccination_by_age[17*i+5]+vaccination_by_age[17*i+6]+vaccination_by_age[17*i+7]+\
                vaccination_by_age[17*i+8]+vaccination_by_age[17*i+9]+vaccination_by_age[17*i+10])
vaccination_18_64=vaccination_18_64[::-1]
vaccination_65_84=[] #everyday number of people vaccinated between 65 and 84
for i in range(0,442):
    vaccination_65_84.append(vaccination_by_age[17*i+11]+vaccination_by_age[17*i+12]+vaccination_by_age[17*i+13]+\
                vaccination_by_age[17*i+14])
vaccination_65_84=vaccination_65_84[::-1]
vaccination_85=[]  #number of people vaccinated above 85
for i in range(0,442):
    vaccination_85.append(vaccination_by_age[17*i+15]+vaccination_by_age[17*i+16])
vaccination_85=vaccination_85[::-1]
    
hospital_admission=np.loadtxt("datasets/hospital_admission.csv",skiprows=1,usecols=(6),unpack=True,delimiter=',')
hospitalization_12_17=[] #everyday number of people sent in hospital between 12 and 17
for i in range(10,716):#There are 716 days in total, and this dataset has 10 days more data than\
    #the previous one, so discard data of these 10 days
    hospitalization_12_17.append((hospital_admission[5*(i)+2]-hospital_admission[5*(i+1)+2])*6/12)
hospitalization_12_17=hospitalization_12_17[::-1]
# (Here we assume the number of people between 6 and 17 are equally spaced)
hospitalization_18_64=[] #everyday number of people sent in hospital between 18 and 64
for i in range(10,716):
    hospitalization_18_64.append((hospital_admission[5*(i)]-hospital_admission[5*(i+1)]))
hospitalization_18_64=hospitalization_18_64[::-1]
hospitalization_65_84=[] #everyday number of people sent in hospital between 65 and 84
for i in range(10,716):
    hospitalization_65_84.append((hospital_admission[5*(i)+4]-hospital_admission[5*(i+1)]+4))
hospitalization_65_84=hospitalization_65_84[::-1]
hospitalization_85=[] #everyday number of people sent in hospital over 85
for i in range(10,716):
    hospitalization_85.append((hospital_admission[5*(i)+3]-hospital_admission[5*(i+1)+3]))
hospitalization_85=hospitalization_85[::-1]   
#%%
#To make the days of vaccination and hospitalization the same, we can add 264 more zeros to the front of the vaccination data
vaccination_12_17=vaccination_12_17[::-1]
for i in range(0,264):
    vaccination_12_17.append(0)
vaccination_12_17=vaccination_12_17[::-1]
vaccination_18_64=vaccination_18_64[::-1]
for i in range(0,264):
    vaccination_18_64.append(0)
vaccination_18_64=vaccination_18_64[::-1]
vaccination_65_84=vaccination_65_84[::-1]
for i in range(0,264):
    vaccination_65_84.append(0)
vaccination_65_84=vaccination_65_84[::-1]
vaccination_85=vaccination_85[::-1]
for i in range(0,264):
    vaccination_85.append(0)
vaccination_85=vaccination_85[::-1]
#%%
dates=np.arange(1,len(vaccination_12_17)+1)
fig,axes=plt.subplots(2,2,figsize=(20,20))
ax1=axes[0,0]
ax2=axes[0,1]
ax3=axes[1,0]
ax4=axes[1,1]
ax1.plot(dates,vaccination_12_17)
ax1.plot(dates,hospitalization_12_17)
ax2.plot(dates,vaccination_18_64)
ax2.plot(dates,hospitalization_18_64)
ax3.plot(dates,vaccination_65_84)
ax3.plot(dates,hospitalization_65_84)
ax4.plot(dates,vaccination_85)
ax4.plot(dates,hospitalization_85)
ax1.title.set_text('number of people between 12 and 17 being vaccinated and hospitalized')
ax2.title.set_text('number of people between 18 and 64 being vaccinated and hospitalized')
ax3.title.set_text('number of people between 65 and 84 being vaccinated and hospitalized')
ax4.title.set_text('number of people over 85 being vaccinated and hospitalized')
ax1.set_xlabel('days since the start of pandemic')
ax2.set_xlabel('days since the start of pandemic')
ax3.set_xlabel('days since the start of pandemic')
ax4.set_xlabel('days since the start of pandemic')
ax1.set_ylabel('number of people')
ax2.set_ylabel('number of people')
ax3.set_ylabel('number of people')
ax4.set_ylabel('number of people')
ax1.legend(['number of people being vaccinated','number of people being hospitalized'])
ax2.legend(['number of people being vaccinated','number of people being hospitalized'])
ax3.legend(['number of people being vaccinated','number of people being hospitalized'])
ax4.legend(['number of people being vaccinated','number of people being hospitalized'])
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.savefig('figures/vaccination_and_hospitalization_plot.png', dpi = 80)
    
