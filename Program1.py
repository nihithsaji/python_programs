startYear=int(input("enter the star year :"))
lastYear=int(input("Enter the last year :"))
endYear=int(input("Enter end year :"))
print("List of leap years")
for Year in range(startYear,endYear):
	if((Year%4==0)and(Year%100!=0))or(Year%400==0):
		print(Year)
