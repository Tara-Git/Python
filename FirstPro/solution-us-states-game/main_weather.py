import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))
# data_dic = data.to_dict()
# print(data_dic)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].max())
# print(max(temp_list))
# print(sum(temp_list) / len(temp_list))
# print(data.condition)

max_temp = data.temp.max()
print(data[data.temp == max_temp])

monday = data[data.day == 'Monday']
print(monday.temp * 9/5 + 32)
dat_dict = {
    'students': ['amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(dat_dict)
print(data)
