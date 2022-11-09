#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Created November 2022
# @author: Aasim Ghaffar
"""

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import requests as rq
import numpy as np
        
def get_data():
    """
    # this function get data from xlsx
    # then store it in data variable and return the data
    """
    
    data = pd.read_excel('data.xlsx')
    
    # return dataframe
    return data

def define_variable(data):
    
    # Define Global Variable
    global years
    global countries
    global data_bel
    global data_can
    global data_ger
    global data_ira
    global data_isr
    
    # Set Graph Data
    data_bel=[data[2016][0],data[2017][0],data[2018][0],data[2019][0],data[2020][0]]
    data_can=[data[2016][1],data[2017][1],data[2018][1],data[2019][1],data[2020][1]]
    data_ger=[data[2016][2],data[2017][2],data[2018][2],data[2019][2],data[2020][2]]
    data_ira=[data[2016][3],data[2017][3],data[2018][3],data[2019][3],data[2020][3]]
    data_isr=[data[2016][4],data[2017][4],data[2018][4],data[2019][4],data[2020][4]]
    
    # Define Years
    years=np.array(['2016', '2017', '2018', '2019', '2020'])
    
    # Define Countries
    countries=np.array(['Belgium', 'Canada', 'Germany', 'Iraq', 'Israel'])
    
def generate_avg(data):
    # Calculating Average
    sum_data = 0
    
    #for loop it will iterate and sum all values
    for t in data:
        sum_data = sum_data + t           

    # Avg variable is used to store average of data
    avg = sum_data / len(data)
    return avg
    
def graph(data,diagram):
    """
    # in this function the visualization take place like
    # Line Chart,
    # Bar Chart,
    # Pie Chart
    """ 
    if diagram=="line":
        
        # here we ploting data
        plt.plot(years,data_bel,label="Belgium")
        plt.plot(years,data_can,label="Canada")
        plt.plot(years,data_ger,label="Germany")
        plt.plot(years,data_ira,label="Iraq")
        plt.plot(years,data_isr,label="Israel")

        # Add labels and title
        plt.title("Plot Multiple lines Data")
        plt.xlabel("Years")
        plt.ylabel("Dealing with construction permits")
         
        # we are adding lagend on upper right
        plt.legend(loc='upper right')
        
        # Generate Chart Image
        plt.savefig('line.png')
        
        # Show graph
        plt.show()
        
    elif diagram=="bar":
    
        # Calculate Average
        average = [generate_avg(data_bel),generate_avg(data_can),generate_avg(data_ger),generate_avg(data_ira),generate_avg(data_isr)]
        
        # Calculate Average set Arrange
        x_pos   = np.arange(len(countries))
        
        # here we bar data
        plt.bar(x_pos,average,color=(0.2,0.1,0.5,0.2))
        
        # Add labels and title
        plt.title("Plot Bar Graph Data")
        plt.xlabel("Countries")
        plt.ylabel("Dealing with construction permits")
        
        # Adding Ticks
        plt.xticks(x_pos, countries)
        
        # Generate Chart Image
        plt.savefig('bar.png')
        
        # Show graph
        plt.show()
        
    elif diagram=="pie":

        # Calculate Average
        average = [generate_avg(data_bel),generate_avg(data_can),generate_avg(data_ger),generate_avg(data_ira),generate_avg(data_isr)]
        
        # here we pie data
        plt.pie(average,labels=countries);
        
        # Add labels and title
        plt.title("Plot Pie Graph Data")
        
        # Generate Chart Image
        plt.savefig('pie.png')
        
        # Show graph
        plt.show()

if __name__=="__main__":
    
    # Get Data   
    data = get_data()
    
    # set variable
    define_variable(data)
    
    # Line Plot Graph
    graph(data,'line')
    
    # Bar Chart Graph
    graph(data,'bar')
    
    # Pie Chart Graph
    graph(data,'pie')