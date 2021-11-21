vac = [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3]
mean = (sum(vac)/len(vac))
lust = []
i = 0
for i in range(len(vac)):
    x = (vac[i] - mean)**2
    lust.append(x)
    avr = (sum(lust) / len(lust))
print(avr)
