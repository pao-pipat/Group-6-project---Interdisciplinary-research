# Interdisciplinary Research Computing project: Validating efficacy and effectiveness of the current COVID-19 vaccines on different age groups 

## A bit about ourselves 
We are four second year students at Imperial College London: Nine Kinnman, Nichakorn Pipatpadungsin (Pao), Jialin Liu (Lester) and Christoforos Georgios Fistouris. Each studying different subject, we brought our skills together, which combined mathematics, medical sciences, and computer science, to create this project studying a global issue that has plagued us for the last two years. Our group advisor, Yiannis Simillides guided us through this project and helped us acheive it.

## Introduction to our interdisciplinary project 
Since the first outbreak of COVID-19 and the start of the pandemic in the start of 2020, governments and various pharmaceutical companies around the world have collaborated for the development of vaccines against COVID-19. The first vaccine to be approved was the CanSino vaccine in China which was used by the military[3]. Since then, various different types of vaccines have been developed from big pharmaceutical companies, such as Pfizer–BioNTech (mRNA vaccine), Johnson & Johnson (modified adenovirus vaccine), AstraZeneca (modified adenovirus vaccine) and Moderna (mRNA vaccine). COVID-19 vaccines have shown to be effective in the protection against the disease. For example, previous clinical trials have shown Pfizer’s vaccine to have up to 95%[1,4]. Nonetheless, these statistics have changed with age and the emergence of variants of concern [2]. Also, it is still difficult to predict the effectiveness of the same vaccine administered to another population [1]. We think investigating and building a model for the observed effectiveness of covid vaccines could be a good start. Therefore, in this project, we aim to produce a statistical model to measure an impact of age as a factor in the vaccines’ effectiveness in protecting against COVID-19.

## Our research question
Can we get the same efficacy and effectiveness of the COVID-19 vaccines observed in the clinical trials using our statistical analysis and does it vary depending on the age of the population receiving it?

## 1. What did we get by just looking at the real-world data?
Before venturing into any complicated data analysis, we think it would be a great starting point to first look at the data available. We managed to retrieve datasets from the NHS for number of cases and vaccinations in the UK (see datasets used) for our analysis. From what we see in the plot (see Figure 1 below) for number of cases and vaccinations against time, 3 peaks of infection can be clearly seen. Roughly starting at the end of the first year of the pandemic, first dose of vaccines are starting to be taken up. This seems to correlate well with the drop of infections. The second dose seems to have further dampened the infection rate during the middle of the second year. However, a small surge of infection rises again in the middle of the second year and it has well been sustained until the third surge of infection towards the end of the second year. Looking at this graph, we can see crude correlations between vaccination rate and infection rate. However, ther might be some caveats such as, for the second and third waves, vaccination rate reaches their peaks before infection rate. This could be because the time needed for the vaccination to develop full immunity within an individual. To see the effect of vaccinations on each age group we then plot another graph for each age group.
![](figures/initial_analysis.png)

## 2. What statastical models did we use?
Using data from the NHS website, we were able to build different statistical models to interpret the data to answer our research question. 

### Vaccination and hospitalization for different age groups

###### **Figure 1** Vaccination compared with hospitalization for different age groups
From the NHS website, we downloaded cumulative number of vaccination and hospitalization data. However, as a lot of data was included which made them quite messy, they needed to be tidied up. To start our analysis, we used the loadtxt function to load all the csv files in python. Then, we noticed that the vaccination data was divided into more age groups than the hospitalization data, so in order to compare these data properly, we combined some of the age groups for the vaccination data. The next problem we encounterded was to work out the daily increase, as these data are all cumulative numbers. So, we used several 'for' loops to take the difference of numbers for each two days. After tidying up our data, we used plt.subplot function to make a plot containing results of four age groups as shown below.
![](figures/vaccination_and_hospitalization_plot.png)

From the graph, we can see that the hospitalization number of young people (people below 65 years old) is constantly low. We can only conclude that the virus does not take a serious form in young people. But if we look at the trend of curves for the last two plots, the hospitalization number reduced significantly after the peak of vaccination, so we can safely conclude that the vaccine is reducing the number of hospitalization. In another word, the vaccine is very effective and is protecting older people from developing serious cases of the disease. 

### Proportion of people taking the vaccine in the UK

###### **Figure 2** People who completed vaccination compared with vaccine registered population in the UK plot
From our downloaded data, we also made a bar chart showing the proportion of people that took the vaccine. 
![](figures/group_figure1.png)

As we can see, the proportion of old people taking the vaccine is relatively higher, and this is consistent with our result from the previous part: old people are at higher risk of serious illness form COVID-19 and the vaccine is effectively protecting old people.

### Statistical analysis for vaccines in the SIR model including vaccination

### How was the model created? ###
The model was built based on the idea of the SIR model used in mathematical biology, where each letter means a different category. "S" stands for Susceptible people, "I" stands for Infected people and finally "R" stands for Recover people. Mathematically, this is solved using ordinary differential equations but first let's try to build this model from scratch. Consider the below diagram:


![SIR MODEL NEW](https://user-images.githubusercontent.com/97306014/159160066-409048fd-7d6d-47c2-97a6-04bdb117194f.png)


Each individual can be only in one compartment at a given time, but can definitely move from one to another. The SIR model is one of the most basic compartmental models, if not the most basic, with 3 compartments (Susceptible, Infected, and Recovered). The assumed progression is for a susceptible individual to become infected through contact with another infected individual. Following a period as an infected individual, during which that person is assumed to be contagious, the individual advances to state, termed recovery.The rate at which susceptible individuals become infected is dependent on the number of individuals in each of the susceptible and infected compartments. At the start of an outbreak, when there are few infected individuals, the disease spreads slowly. As more individuals become infected, they contribute to the spread and increase the rate of infection. An additional factor in calculating the rate of spread is the effective contact rate (β). This parameter accounts for the transmissibility of the disease. Community mitigation strategies, such as quarantining infected individuals, social distancing, and closing schools, reduce this value and therefore slow the spread. Although these interventions can alter the movement of individuals from the susceptible compartment to the infected compartment, the transition from the infected to the recovered compartment is solely dependent on the amount of time that an individual is contagious, captured in the rate of recovery (γ).
This model contains only 2 parameters: the effective contact rate (β), which affects the transition from the susceptible compartment to the infected compartment, and the rate of recovery (or mortality; γ), which affects the transition from the infected compartment to the recovered compartment.
If the rate at which individuals become infected exceeds the rate at which infected individuals recover, there will be an accumulation of individuals in the infected compartment. The basic reproduction number R0, the mean number of new infections caused by a single infected individual over the course of their illness, is the ratio between β and γ. A decrease in the effective contact rate β through community mitigation strategies decreases R0, delaying and lowering the peak infection rate that occurs in the epidemic (ie, “flattening the curve”). However, to maintain the decrease in total infections, the decrease in R0 generally must be sustained.
Our new model, with vaccination was based on the SIR model but we added the compartment of " Vaccinated people". Since more people are vaccinated, the infected people would get reduced since they have immunity by the vaccine. The differential equation characterized the Vaccinated state is that the rate of change of vaccinated people equals with the starting of vaccinated people plus a constant of vaccine efficiency times the number of Susceptible people times the time interval that vaccination occurs. With all these features, we made a stasticial analysis and created graphs for the COVID-19 pandemic before and after vacciantion.

###### **Figure 3** Modified SIR Model for 2 years of pandemic
