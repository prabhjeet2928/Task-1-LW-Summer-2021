import pandas
import os
ds = pandas.read_csv('SalaryData.csv')
x = ds['YearsExperience'].values.reshape(30,1)
y = ds['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
while True:
	print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
	print("                                                                                           ")
	print("                               LINEAR REGRESSION IN DOCKER                                 ")
	print("                                                                                           ")
	print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
	years = float(input("Enter your years of experience: "))
	predict = model.predict([[years]])
	print("The {} years experience salary is: ".format(years) ,predict)
	while True:
		final = input("\nPress Enter key to continue or 'exit' to exit the ML LR Program: ")
		if final == "exit":
			print()
			print("\t\t\t\t\tTHANK YOU\n")
			exit()
		elif final == "":
			break
		else:
			print("\nPlease put correct data")
