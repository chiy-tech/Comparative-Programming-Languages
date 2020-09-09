import covid_stat
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time

def strToDatetime(string):
    Datetime = datetime.datetime.strptime(string,'%Y-%m-%d')
    return Datetime
def to_timestamp(datetime):
    stamp = time.mktime(time.strptime(datetime.strftime('%Y-%m-%d'), '%Y-%m-%d'))
    return stamp
data = pd.read_csv('owid-covid-data.csv')
us_data = data[data.iso_code == 'USA']

us_data['date'] = us_data['date'].apply(strToDatetime)
us_data['timestamp'] = us_data['date'].apply(to_timestamp)
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(us_data['date'],us_data['total_cases'],label='total_cases')
plt.xlabel('Date')
plt.ylabel('Numbers')
plt.legend()
#plt.show()
cad_data = data[data.iso_code == 'CAN']

cad_data['date'] = cad_data['date'].apply(strToDatetime)
cad_data['timestamp'] = cad_data['date'].apply(to_timestamp)
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(cad_data['date'],cad_data['total_cases'],label='total_cases')
plt.xlabel('Date')
plt.ylabel('Numbers')
#plt.show()

nzl_data = data[data.iso_code == 'NZL']
nzl_data['date'] = nzl_data['date'].apply(strToDatetime)
nzl_data['timestamp'] = nzl_data['date'].apply(to_timestamp)
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(nzl_data['date'],nzl_data['total_cases'])
plt.xlabel('Date')
plt.ylabel('Numbers')
#plt.show()


world_data = data[data.location == 'World']
world_data['date'] = world_data['date'].apply(strToDatetime)
world_data['timestamp'] = world_data['date'].apply(to_timestamp)
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(world_data['date'],world_data['total_cases'])
plt.xlabel('Date')
plt.ylabel('Numbers')
#plt.show()

plt.title("Total cases")
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.subplot(221)
plt.plot(us_data['date'],us_data['total_cases'],label='us_total_cases')
plt.legend()
plt.xlabel('Month')
plt.ylabel('us_rate')
plt.subplot(222)
plt.plot(cad_data['date'],cad_data['total_cases'],label='cad_total_cases')
plt.legend()
plt.xlabel('Month')
plt.ylabel('cad_rate')
plt.subplot(223)
plt.plot(nzl_data['date'],nzl_data['total_cases'],label='nzl_total_cases')
plt.legend()
plt.xlabel('Month')
plt.ylabel('nzl_rate')
plt.subplot(224)
plt.plot(world_data['date'],world_data['total_cases'],label='world_total_cases')
plt.legend()
plt.xlabel('Month')
plt.ylabel('world_rate')

plt.savefig("All_total_cases.png")

plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(us_data['date'],us_data['total_cases'],label='USA_total_cases')
plt.plot(cad_data['date'],cad_data['total_cases'],label='CAN_total_cases')
plt.plot(nzl_data['date'],nzl_data['total_cases'],label='NZL_total_cases')
plt.plot(world_data['date'],world_data['total_cases'],label='World_total_cases')
plt.xlabel('Date')
plt.ylabel('Numbers')
plt.legend()



print("============================================================")
print("USA:")
mar1= us_data[us_data.date == "2020-03-01"]["total_cases"].iloc[0]
mar2 = us_data[us_data.date == "2020-03-31"]["total_cases"].iloc[0]
rateofMar = covid_stat.rateOfMonth(mar1,mar2)
print("The growth rate of March is:",rateofMar)
Apr1= us_data[us_data.date == "2020-04-01"]["total_cases"].iloc[0]
Apr2 = us_data[us_data.date == "2020-04-30"]["total_cases"].iloc[0]
rateofApr = covid_stat.rateOfMonth(Apr1,Apr2)
print("The growth rate of April is:",rateofApr)
may1= us_data[us_data.date == "2020-05-01"]["total_cases"].iloc[0]
may2 = us_data[us_data.date == "2020-05-31"]["total_cases"].iloc[0]
rateofmay = covid_stat.rateOfMonth(may1,may2)
print("The growth rate of May is:",rateofmay)
jun1= us_data[us_data.date == "2020-06-01"]["total_cases"].iloc[0]
jun2 = us_data[us_data.date == "2020-06-30"]["total_cases"].iloc[0]
rateofjun = covid_stat.rateOfMonth(jun1,jun2)
print("The growth rate of June is:",rateofjun)
jul1= us_data[us_data.date == "2020-07-01"]["total_cases"].iloc[0]
jul2 = us_data[us_data.date == "2020-07-31"]["total_cases"].iloc[0]
rateofjul = covid_stat.rateOfMonth(jul1,jul2)
print("The growth rate of July is:",rateofjul)
aug1= us_data[us_data.date == "2020-08-01"]["total_cases"].iloc[0]
aug2 = us_data[us_data.date == "2020-08-16"]["total_cases"].iloc[0]
rateofaug = covid_stat.rateOfMonth(aug1,aug2)
print("The growth rate of Augest is:",rateofaug)

usa_rate = [rateofApr,rateofmay,rateofjun,rateofjul,rateofaug]
index = ["4","5","6","7","8"]
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(index,usa_rate)
plt.xlabel('Month')
plt.ylabel('usa_rate')
#plt.savefig("usa_rate.png")
res =covid_stat.avgRateOfMonth(rateofApr,rateofmay,rateofjun,rateofjul,rateofaug)
print("The average growth from April to Augest is:",res)





print("============================================================")
print("CAN:")
mar1= cad_data[cad_data.date == "2020-03-01"]["total_cases"].iloc[0]
mar2 = cad_data[cad_data.date == "2020-03-31"]["total_cases"].iloc[0]
rateofMar = covid_stat.rateOfMonth(mar1,mar2)
print("The growth rate of March is:",rateofMar)
Apr1= cad_data[cad_data.date == "2020-04-01"]["total_cases"].iloc[0]
Apr2 = cad_data[cad_data.date == "2020-04-30"]["total_cases"].iloc[0]
rateofApr = covid_stat.rateOfMonth(Apr1,Apr2)
print("The growth rate of April is:",rateofApr)
may1= cad_data[cad_data.date == "2020-05-01"]["total_cases"].iloc[0]
may2 = cad_data[cad_data.date == "2020-05-31"]["total_cases"].iloc[0]
rateofmay = covid_stat.rateOfMonth(may1,may2)
print("The growth rate of May is:",rateofmay)
jun1= cad_data[cad_data.date == "2020-06-01"]["total_cases"].iloc[0]
jun2 = cad_data[cad_data.date == "2020-06-30"]["total_cases"].iloc[0]
rateofjun = covid_stat.rateOfMonth(jun1,jun2)
print("The growth rate of June is:",rateofjun)
jul1= cad_data[cad_data.date == "2020-07-01"]["total_cases"].iloc[0]
jul2 = cad_data[cad_data.date == "2020-07-31"]["total_cases"].iloc[0]
rateofjul = covid_stat.rateOfMonth(jul1,jul2)
print("The growth rate of July is:",rateofjul)
aug1= cad_data[cad_data.date == "2020-08-01"]["total_cases"].iloc[0]
aug2 = cad_data[cad_data.date == "2020-08-16"]["total_cases"].iloc[0]
rateofaug = covid_stat.rateOfMonth(aug1,aug2)
print("The growth rate of Augest is:",rateofaug)

can_rate = [rateofApr,rateofmay,rateofjun,rateofjul,rateofaug]
index = ["4","5","6","7","8"]
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(index,can_rate)
plt.xlabel('Month')
plt.ylabel('can_rate')
#plt.savefig("can_rate.png")
res =covid_stat.avgRateOfMonth(rateofApr,rateofmay,rateofjun,rateofjul,rateofaug)
print("The average growth from April to Augest is:",res)


print("============================================================")
print("NZL:")
mar1= nzl_data[nzl_data.date == "2020-03-01"]["total_cases"].iloc[0]
mar2 = nzl_data[nzl_data.date == "2020-03-31"]["total_cases"].iloc[0]
rateofMar = covid_stat.rateOfMonth(mar1,mar2)
print("The growth rate of March is:",rateofMar)
Apr1= nzl_data[nzl_data.date == "2020-04-01"]["total_cases"].iloc[0]
Apr2 = nzl_data[nzl_data.date == "2020-04-30"]["total_cases"].iloc[0]
rateofApr = covid_stat.rateOfMonth(Apr1,Apr2)
print("The growth rate of April is:",rateofApr)
may1= nzl_data[nzl_data.date == "2020-05-01"]["total_cases"].iloc[0]
may2 = nzl_data[nzl_data.date == "2020-05-31"]["total_cases"].iloc[0]
rateofmay = covid_stat.rateOfMonth(may1,may2)
print("The growth rate of May is:",rateofmay)
jun1= nzl_data[nzl_data.date == "2020-06-01"]["total_cases"].iloc[0]
jun2 = nzl_data[nzl_data.date == "2020-06-30"]["total_cases"].iloc[0]
rateofjun = covid_stat.rateOfMonth(jun1,jun2)
print("The growth rate of June is:",rateofjun)
jul1= nzl_data[nzl_data.date == "2020-07-01"]["total_cases"].iloc[0]
jul2 = nzl_data[nzl_data.date == "2020-07-31"]["total_cases"].iloc[0]
rateofjul = covid_stat.rateOfMonth(jul1,jul2)
print("The growth rate of July is:",rateofjul)
aug1= nzl_data[nzl_data.date == "2020-08-01"]["total_cases"].iloc[0]
aug2 = nzl_data[nzl_data.date == "2020-08-16"]["total_cases"].iloc[0]
rateofaug = covid_stat.rateOfMonth(aug1,aug2)
print("The growth rate of Augest is:",rateofaug)

nzl_rate = [rateofApr,rateofmay,rateofjun,rateofjul,rateofaug]
index = ["4","5","6","7","8"]
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(index,nzl_rate)
plt.xlabel('Month')
plt.ylabel('nzl_rate')
#plt.savefig("nzl_rate.png")
res =covid_stat.avgRateOfMonth(rateofApr,rateofmay,rateofjun,rateofjul,rateofaug)
print("The average growth from April to Augest is:",res)

print("============================================================")
print("World:")
mar1= world_data[world_data.date == "2020-03-01"]["total_cases"].iloc[0]
mar2 = world_data[world_data.date == "2020-03-31"]["total_cases"].iloc[0]
rateofMar = covid_stat.rateOfMonth(mar1,mar2)
print("The growth rate of March is:",rateofMar)
Apr1= world_data[world_data.date == "2020-04-01"]["total_cases"].iloc[0]
Apr2 = world_data[world_data.date == "2020-04-30"]["total_cases"].iloc[0]
rateofApr = covid_stat.rateOfMonth(Apr1,Apr2)
print("The growth rate of April is:",rateofApr)
may1= world_data[world_data.date == "2020-05-01"]["total_cases"].iloc[0]
may2 = world_data[world_data.date == "2020-05-31"]["total_cases"].iloc[0]
rateofmay = covid_stat.rateOfMonth(may1,may2)
print("The growth rate of May is:",rateofmay)
jun1= world_data[world_data.date == "2020-06-01"]["total_cases"].iloc[0]
jun2 = world_data[world_data.date == "2020-06-30"]["total_cases"].iloc[0]
rateofjun = covid_stat.rateOfMonth(jun1,jun2)
print("The growth rate of June is:",rateofjun)
jul1= world_data[world_data.date == "2020-07-01"]["total_cases"].iloc[0]
jul2 = world_data[world_data.date == "2020-07-31"]["total_cases"].iloc[0]
rateofjul = covid_stat.rateOfMonth(jul1,jul2)
print("The growth rate of July is:",rateofjul)
aug1= world_data[world_data.date == "2020-08-01"]["total_cases"].iloc[0]
aug2 = world_data[world_data.date == "2020-08-16"]["total_cases"].iloc[0]
rateofaug = covid_stat.rateOfMonth(aug1,aug2)
print("The growth rate of Augest is:",rateofaug)

world_rate = [rateofApr,rateofmay,rateofjun,rateofjul,rateofaug]
index = ["4","5","6","7","8"]
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(index,world_rate)
plt.xlabel('Month')
plt.ylabel('world_rate')
#plt.savefig("world_rate.png")
res =covid_stat.avgRateOfMonth(rateofApr,rateofmay,rateofjun,rateofjul,rateofaug)
print("The average growth from April to Augest is:",res)

#print(usa_rate,can_rate,nzl_rate,world_rate)

world_rate = [rateofApr,rateofmay,rateofjun,rateofjul,rateofaug]
index = ["4","5","6","7","8"]
plt.figure(figsize=(16,9))
plt.xticks(rotation=25)
plt.plot(index,usa_rate,label = "usa_rate")
plt.plot(index,can_rate,label = "can_rate")
plt.plot(index,nzl_rate,label = "nzl_rate")
plt.plot(index,world_rate,label = "world_rate")
plt.legend()
plt.xlabel('Month')
plt.ylabel('all_rate')


plt.figure(figsize=(16,9))
plt.title("Growth rate")
plt.xticks(rotation=25)
plt.subplot(221)
plt.plot(index,usa_rate,label = "usa_growth_rate")
plt.legend()
plt.xlabel('Month')
plt.ylabel('us_rate')
plt.subplot(222)
plt.plot(index,can_rate,label = "can_growth_rate")
plt.legend()
plt.xlabel('Month')
plt.ylabel('cad_rate')
plt.subplot(223)
plt.plot(index,nzl_rate,label = "nzl_growth_rate")
plt.legend()
plt.xlabel('Month')
plt.ylabel('nzl_rate')
plt.subplot(224)
plt.plot(index,world_rate,label = "world_growth_rate")
plt.legend()
plt.xlabel('Month')
plt.ylabel('world_rate')
plt.savefig("all_growth_rate.png")


