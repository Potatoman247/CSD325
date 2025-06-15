import csv
from tkinter import *
from datetime import datetime

from matplotlib import pyplot as plt

def highs():
    # Get dates and high temperatures from this file.
    dates, highs = [], []
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)

    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def lows():
    dates, lows = [], []
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as g:
        reader = csv.reader(g)
        header_row = next(reader)
    # Get dates and low temperatures from this file.
    
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            low = int(row[6])
            lows.append(low)

    # Plot the low temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()    
    
def main():
        root = Tk()
        root.title("Title")
        #root.geometry('400x300')
        
        btn1 = Button(root,text = "HIGHS", fg = 'red', command=highs)
        btn1.grid(column = 1, row = 0)  
        
        btn2 = Button(root,text = "LOWS", fg = 'red', command=lows)
        btn2.grid(column = 3, row = 0)         
        root.mainloop()
main()