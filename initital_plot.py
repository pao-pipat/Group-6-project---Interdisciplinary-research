"""Plotting for initial analysis"""
from pylab import *
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib as mpl

#import datasets
daily_cases = pd.read_csv('datasets/daily_cases_03022022.csv')
daily_cases_dates = daily_cases.loc[:, ['date', 'newCasesBySpecimenDate']]

first_dose = pd.read_csv('datasets/vaccination_first_dose_new.csv')
first_dose_dates = first_dose.loc[:, ['date', 'newPeopleVaccinatedFirstDoseByPublishDate']]

second_dose = pd.read_csv('datasets/vaccination_second_dose.csv')
second_dose_dates = second_dose.loc[:, ['date', 'newPeopleVaccinatedSecondDoseByPublishDate']]

third_dose = pd.read_csv('datasets/vaccination_third_dose_new.csv')
third_dose_dates = third_dose.loc[:, ['date', 'newPeopleVaccinatedThirdInjectionByPublishDate']]

#creating dataframe for plot
plot_df = pd.merge(daily_cases_dates, first_dose_dates, how='outer', on = 'date')
plot_df = pd.merge(plot_df, second_dose_dates, how='outer', on = 'date')
plot_df = pd.merge(plot_df, third_dose_dates, how='outer', on = 'date')
plot_df = plot_df.drop(761) #This row is not included due to insufficient data
plot_df = plot_df.sort_values('date')

#Add new column: daysAfterFirstOutbreak for plotting
daysAfterFirstOutbreak = []
for i in range(len(plot_df)):
    daysAfterFirstOutbreak.append(i)
plot_df['daysAfterFirstOutbreak'] = daysAfterFirstOutbreak



#save dataframe
to_save = Path('datasets/plot_df.csv')
to_save.parent.mkdir(parents = True, exist_ok = True)
plot_df.to_csv(to_save)

#plot
figure(figsize = (15,9), dpi = 80)
plot(plot_df['daysAfterFirstOutbreak'],plot_df['newCasesBySpecimenDate'], 
color = 'darkred', label = 'Daily Cases')
plot(plot_df['daysAfterFirstOutbreak'],plot_df['newPeopleVaccinatedFirstDoseByPublishDate'], 
color = 'lightblue', label = 'First Dose')
plot(plot_df['daysAfterFirstOutbreak'],plot_df['newPeopleVaccinatedSecondDoseByPublishDate'], 
color = 'blue', label = 'Second Dose')
plot(plot_df['daysAfterFirstOutbreak'],plot_df['newPeopleVaccinatedThirdInjectionByPublishDate'], 
color = '#24B1E0', label = 'Third Dose')
legend = plt.legend(loc='upper left')
xlabel('days after first outbreak', fontsize = 12)
xticks(np.arange(0, len(plot_df['daysAfterFirstOutbreak']), 30.0))
xticks(rotation = 50)
ylabel('number of individuals', fontsize = 12)
title('COVID-19 reported daily cases and daily vaccinations in the UK', fontsize = 16)
ticklabel_format(style='scientific')
subplots_adjust(top=0.94,
bottom=0.15,
left=0.1,
right=0.94,
hspace=0.1,
wspace=0.1)
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False


#save figure
savefig('figures/initial_analysis.png', dpi = 80)