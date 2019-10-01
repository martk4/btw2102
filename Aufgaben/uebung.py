



i = 31719845 
#i=31536000
#i=90000

#Try 1
#years = int(i/(365*24*3600))
#days = int(i/(3600*24))- (years*365) 
#hours = int(i/3600)- (days*24)
#minutes = int((i/60)-hours*60)
#seconds = i- ((minutes *60)- (hours*60)-)

#Try 2
#years=int(i/(365*24*3600))
#hours=int(i/3600)- (years*365*24*3600)-(days*24*3600)
#days=int(i/(24*3600))-(years*365*24*3600)
#minutes=int(i/60) - (years*365*24*3600)-(days*24*3600)-(hours*3600)
#seconds= i- (years*365*24*3600)-(days*24*3600)-(hours*3600) - (minutes*60)

#Solution

years = int(i/(86400*365))
days = int(i % (86400*365)/86400)
hours = int((i % 86400)/3600)
minutes = int((i % 3600)/60)
seconds = i%60

print(f"Years: {years} \t Days: {days} \t Hours: {hours} \t Minutes: {minutes} \t Seconds: {seconds}")

print("\nIn other words:\n")

sec_y = 86400*365
sec_d = 86400
sec_h = 3600
sec_m = 60

years = int(i/(sec_y))
days = int((i % sec_y)/sec_d)
hours = int((i % sec_d)/sec_h)
minutes = int((i % sec_h)/sec_m)
seconds = i%sec_m

print(f"Years: {years} \t Days: {days} \t Hours: {hours} \t Minutes: {minutes} \t Seconds: {seconds}")
