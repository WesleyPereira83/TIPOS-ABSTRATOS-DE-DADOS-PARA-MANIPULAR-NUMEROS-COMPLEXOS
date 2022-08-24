#Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
#O método deve:

#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números. 

from abc import ABC, abstractmethod


class NumerosComplexos:
    
    def __init__(self, v1, v2, v3, v4, v5, v6):
      
        self.valor1 = v1
        self.valor2 = v2
        self.valor3 = v3
        self.valor4 = v4
        self.valor5 = v5
        self.valor6 = v6
           
    def Soma(self):      
        
        self.resultado1 = (self.valor1) + (self.valor3) + (self.valor5)
        self.resultado2 = (self.valor2) + (self.valor4) + (self.valor6)
      
       
v1 = float(input('Insira o numero real da equação Z1\n'))
v2 = float(input('Insira o numero imaginário da equação Z1\n'))  

v3 = float(input('Insira o numero real da equação Z2\n'))
v4 = float(input('Insira o numero imaginário da equação Z2\n'))  

v5 = float(input('Insira o numero real da equação Z3\n'))
v6 = float(input('Insira o numero imaginário da equação Z3\n'))  
print(' ')

a = NumerosComplexos(v1 , v2, v3, v4, v5, v6)

a.Soma()
print(f'Parte real da Z1 =', a.valor1)
print(f'Parte imaginária Z1 =', a.valor2,'i\n')
print(f'Parte real Z2 =', a.valor3)
print(f'Parte imaginária Z2 =', a.valor4,'i\n')
print(f'Parte real Z3 =', a.valor5)
print(f'Parte imaginária Z3 =', a.valor6,'i\n')

print(f'Somando as equações:', '(Z1 =',v1, '+', v2,'i)', ';', '(Z2 =',v3, '+', v4,'i)', 'e' , '(Z3 =',v5,'+',v6,'i)',':\n')
print(f'A soma da parte real do número complexo é =', a.resultado1, '.\n')
print(f'A soma da parte imaginaria do número complexo é =', a.resultado2, '.\n')
print(f'Equação final: (Z =', a.resultado1, '+', a.resultado2,'i) \n')
      

