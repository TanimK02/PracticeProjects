# import csv
#
# with open('weather_data.csv','r') as days:
#     data = csv.reader(days)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(row[1])
#
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# # print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(data['temp'].mean())
#
# print(data['temp'].max())
#
# #get data in columns
# print(data.condition)
#
# #get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# print(monday.condition)
# monday_temp_f = (monday['temp'] * 9/5) + 32
# print(monday_temp_f)
#
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')




gray = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

color_dict = {
    'Fur Color': ['gray', 'cinnamon', 'black'],
    'count': [gray,cinnamon,black]

}

squirrel_colors = pandas.DataFrame(color_dict)
squirrel_colors.to_csv('squirrel_count.csv')

