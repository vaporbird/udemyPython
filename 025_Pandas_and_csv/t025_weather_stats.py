#with open("weather_data.csv", mode = "r") as file:
#	data = file.readlines()
#	print(data)
#********************************************************************
#import csv
#temperatures = []
#with open("weather_data.csv", mode = "r") as file:
#	data = csv.reader(file)
#	for row in data:
#		print(row)
#		try:
#			temperatures.append(int(row[2]))
#		except Exception:
#			pass
#print(temperatures)
#********************************************************************
import pandas
import numpy
data = pandas.read_csv("weather_data.csv")
print(data)
temps = data["temp"]
#********************************************************************
#acc = 0
#acc = sum(temps)
#avg = acc/len(temps)
#print(avg)
#********************************************************************
data_dict = data.to_dict()
print(data_dict["temp"])

total = sum(data_dict["temp"].values())
avg = total/len(data_dict["temp"])
print(avg)

data_list = data["temp"].to_list()
print(data_list)

print(data_dict.items())
print(f"\n\n\n\nmax_temp : {data['temp'].max()}")


#print(data.condition)
#print(data.iloc[0])
#print(data[data.day == "Monday"])

print("\n\n\n\n")
#print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.temp * 1.8 + 32)

