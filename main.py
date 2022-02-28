"""Statistical analysis for vaccines."""
import matplotlib.pyplot as plt
import numpy as np
import csv

file = open('vaccination by age group.csv')

csvreader = csv.reader(file)

class Data_Analysis:
    
    def __init__(self):