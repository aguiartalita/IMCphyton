altura = float(input('Qual é  a sua altura em cm:'))
peso = float(input('Qual é o seu peso em kls:'))

IMC = peso / (altura/100)** 2

print(IMC)

if IMC < 18.5:
  print(f"Seu IMC é de {IMC}, e é classificado como magreza" )
  
elif IMC >= 18.5 and IMC  < 24.9:
 print (f"Seu IMC é de {IMC}, e é classificado como normal")

elif IMC >= 25 and IMC < 29.9:
   print (f"Seu IMC é de {IMC}, e é classificado como Sobrepeso")

elif IMC >= 30 and IMC < 39.9: 
 print (f"Seu IMC é de {IMC}, e é classificado como Obesidade")

else: 
 print ("Obsidade Grave III !!! Procure um médico caso sinta a necessidade")



