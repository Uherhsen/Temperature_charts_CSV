# -*- coding: utf-8 -*-
"""
Функция 
"""

from datetime import datetime
import csv

def celsiy(y):
    x = (y-32)//1.8
    return x

def dates_highs_lows(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        
        dates, highs , lows = [],[],[]
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                hight = celsiy(int(row[1]))
                low = celsiy(int(row[3]))
            except ValueError:
                print(current_date, 'в этой точке не хватает данных, она будет пропущена')
            else:
                dates.append(current_date) 
                highs.append(hight)
                lows.append(low)
                
    return dates, highs , lows

if __name__ == "__main__":
    d_h_l = dates_highs_lows('data/sitka_weather_2014.csv')
    d,h,l= d_h_l
    print ('data=',d[0:3],'highs=',h[0:3],'lows=',l[0:3])