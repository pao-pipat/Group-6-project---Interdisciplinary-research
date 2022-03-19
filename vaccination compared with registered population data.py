# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:05:56 2022

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
register_population=np.loadtxt("vaccination_by_age_group.csv",skiprows=1,usecols=(5),unpack=True,delimiter=',')
cum_vaccinated_complete=np.loadtxt("vaccination_by_age_group.csv",skiprows=1,usecols=(6),unpack=True,delimiter=',')
age_group=['12-15','16-17','18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90+']
register_population_1=register_population[:17]
cum_vaccinated_completed_1=cum_vaccinated_complete[:17]
ind=np.arange(len(register_population_1))
width=0.35
plt.bar(ind,register_population_1,width,label='Registered population')
plt.bar(ind+width,cum_vaccinated_completed_1,width,label='Completed vaccinated population')
plt.xticks(ind+width/2,age_group)
plt.xticks(rotation=60)
plt.ylabel('Number of people')
plt.title('People who completed vaccination compared with\n vaccine registered population in UK')
plt.legend(loc='best')
plt.show()

savefig('figures/group_figure1.png', dpi = 80)