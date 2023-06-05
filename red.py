import random
              
              
entrada1 = 0
entrada2 = 0
entrada3= 0


peso1=0
peso2=0
peso3=0
umbral=0.123897

#! Feed Fowar
salida = entrada1*peso1+ entrada2*peso2+entrada3*peso3
salida +=umbral 

print (salida)            
              
              
entradas =[0, 0,0]
pesos=  [0,0,0,0.123897]            
  
salida = entradas[0]*pesos[0]+ entradas[1]*pesos[1] +  entradas[2]*pesos[2]         
salida+=pesos[-1]
       
print(salida)     


#*Optimizacion 2 

entradas2 =[0,0,0]
pesos2=  [0,0,0,0.123897] 
salida3=0

for i in range(len(entradas2)) :
    salida3 += entradas2[i]*pesos2[i]        
  
salida3+=pesos2[-1]
print(salida3)  