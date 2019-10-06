days_in_year = 365

total_days = 0

for year in range (1900,2020):
        total_days=total_days+days_in_year
        if year %4 == 0 and year % 400 != 0 :
            total_days +=1
print ("Sundays: ",end="")
print(total_days // 7)