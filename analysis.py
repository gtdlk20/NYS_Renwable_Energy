import pandas as pd
import matplotlib.pyplot as plt
import math

ny = pd.read_csv('NYC_energy.csv')
nyDict = dict()
for i, j in ny.iteritems():
    nyDict[i] = list(j)

renewables = [0] * 57
nonrenew = [0] * 57
for key in nyDict.keys():
    if key in ['Wind  ', 'Solar', 'Conv. Hydro  ', 'PS Hydro  ', 'Waste  ', 'Wood  ', 'LFG  ']:
        for i, x in enumerate(nyDict[key]):
            if not math.isnan(x):
                renewables[i] += x
    elif not key in ['Year', 'Total  ']:
        for i, y in enumerate(nyDict[key]):
            if not math.isnan(y):
                nonrenew[i] += y
print(renewables)

percentRenew = [x / y for x, y in zip(renewables, nyDict['Total  '])]


#plot percent renewables
plt.figure(1)
plt.plot(nyDict['Year'], percentRenew)
plt.title('% Renewables in NY Total Energy Mix')
plt.show()

#plot percent renewables versus percent nuclear/fossil
plt.figure(2, figsize=(8, 8))
plt.subplot(1,2,1)
nuclear = [x/y for x, y in zip(nyDict['Nuclear  '], nyDict['Total  ']) if not math.isnan(x)]
plt.plot(nyDict['Year'], percentRenew, label='Renewables')
plt.plot(nyDict["Year"], nuclear, label='Nuclear')
plt.legend(loc='upper left')
plt.title('Percentage Renewables vs. Nuclear')

plt.subplot(1,2,2)
percentFossil = [x/t for x, t in zip(nyDict['Coal  '], nyDict['Total  ']) if not math.isnan(x)]
for i, t in zip(range(len(percentFossil)), nyDict['Total  ']):
    if not math.isnan(nyDict['Petroleum  '][i]):
        percentFossil[i] += nyDict['Petroleum  '][i]/t
    if not math.isnan(nyDict['Natural Gas  '][i]):
        percentFossil[i] += nyDict['Natural Gas  '][i]/t



plt.plot(nyDict['Year'][:37], percentRenew[:37], label='Renewables')
plt.plot(nyDict['Year'][:37], percentFossil, alpha=.5, label='Fossil Fuels')
plt.title('Percentage Renewables vs. Fossil Fuels')
plt.legend(loc='upper right')
plt.xlabel('*Fossil Fuel data only dates back to 1980')
plt.subplots_adjust(wspace=.5)
plt.show()


#plot 3: pie charts showing composition of renewable sources over time

for i, yr in enumerate([1,11,21,31,41,51]):
    year = nyDict['Year'][yr]
    values = []
    label = []
    for key in ['Wind  ', 'Solar', 'Conv. Hydro  ', 'PS Hydro  ', 'Waste  ', 'Wood  ', 'LFG  ']:
        x = nyDict[key][yr]
        if not math.isnan(x) and x != 0:
            values.append(x)
            label.append(key.strip())
    plt.figure(3+i, figsize=(6, 6))
    plt.pie(values, labels=label)

    plt.title(str(year))
plt.show()




