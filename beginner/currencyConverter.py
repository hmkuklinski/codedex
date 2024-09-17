#money converter
pesos=int(input('what do you have left in pesos?'))
reais= int(input('what do you have left in reais?'))
soles= int(input('what do you ahve left in soles?'))

pesosConversionRate= 0.059 #mexico
reaisConversionRate=0.20 #brazil
solesConversionRate=0.27 #peru

pesoConverted= pesos*pesosConversionRate
reaisConverted= reais*reaisConversionRate
solesConverted= soles*solesConversionRate

totalUSD= pesoConverted+reaisConverted+solesConverted
print(totalUSD)