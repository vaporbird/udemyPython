import datetime
from dateutil.relativedelta import relativedelta 
birthday = datetime.datetime(2000,1,1) #obviously i'm not giving my real birthday :)
death = birthday + relativedelta(years=91)
print(f"You will die on {death} ")
weeksTotal = weeksLeft = weeksLived = 0
while(death > birthday + relativedelta(weeks=weeksTotal)):
	weeksTotal+=1
	if(datetime.datetime.today() > birthday + relativedelta(weeks=weeksTotal)):
		weeksLived += 1
		continue
	weeksLeft += 1
		
print(f"You have lived {weeksLived} out of {weeksTotal} weeks and have {weeksLeft} left to live :)")
