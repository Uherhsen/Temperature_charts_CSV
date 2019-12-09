# -*- coding: utf-8 -*-
"""
Metiz s 326- 
Chapter 16
Работа с даными ыормата CSV, погода в разных точках
!!! Вспоминаем конструкцию enumerate
"""
from matplotlib import pyplot as plt
#from datetime import datetime # модули стали не нужны так как они импортируются в highs_lows_lists 
#import csv  # модули стали не нужны так как они импортируются в highs_lows_lists 
from highs_lows_lists import dates_highs_lows as d_h_l


dates1,highs1,lows1= d_h_l('data/sitka_weather_2014.csv') # Используем функцию из модуля highs_lows_lists
dates2,highs2,lows2= d_h_l('data/death_valley_2014.csv')  # Используем функцию из модуля highs_lows_lists 


# Чтение дат и температурных максимумов из файла.
#filename = 'data/sitka_weather_2014.csv'
#with open(filename) as f:
#    reader = csv.reader(f)
#    header_row = next(reader)
    #print(header_row)
'''   
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)
'''
#    dates, highs , lows = [],[],[]
#    for row in reader:
#        try:
#            current_date = datetime.strptime(row[0], "%Y-%m-%d")
#            hight = int(row[1])
#            low = int(row[3])
#        except ValueError:
#            print(current_date, 'Не хватает данных')
#        else:
#            dates.append(current_date) 
#            highs.append(hight)
#            lows.append(low)


# Нанесение данных на диаграмму:
fig = plt.figure(dpi=128, figsize=(10,6))
ax = fig.add_subplot(111) # цифыры масштаб x, у, четверти квадрата (от 1 до 4 )   

xax = ax.xaxis   # или xax = ax.get_xaxis()

# Линии вспомогательной сетки (главные деления) только по оси абсцисс
xax.grid(True)

plt.plot(dates1,highs1, c='red') # НАнесем первый график - мак дневн темп
plt.plot(dates1,lows1, c='green') # Нанесем второй график - мин дневн температурн
plt.fill_between(dates1, highs1, lows1,facecolor='blue', alpha=0.2) # Затушевать диапазон

plt.plot(dates2,highs2, c='purple') # НАнесем первый график - мак дневн темп
plt.plot(dates2,lows2, c='blue') # Нанесем второй график - мин дневн температурн
plt.fill_between(dates2, highs2, lows2, facecolor='green', alpha=0.2) # Затушевать диапазон

# Форматитирование диаграммы:
plt.title('Макс. и мин. дневн. температуры 2014\n', fontsize=20)
plt.xlabel('',fontsize=14)

fig.autofmt_xdate() # Создаёт наклон по оси х
plt.ylabel("Температура (гр C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
