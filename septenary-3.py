
from time import sleep
user= int(input("\033[30;m Digite um valor:  \033[m"))
print("\033[35;m Escolha um das bases de conversão: \033[m")

print("\033[30;m [1] Conversão  para BINÁRIO")

print(" [2] Conversão  para OCTAL")

print(" [3] Conversão  para HEXADECIMAL \033[m")

op = int(input("\033[35;m OPÇÃO:\033[;m"))

print("\033[30;m Processando...\033[m")
sleep(2)

if op == 1:
    print("\033[30;m Seu valor em binário fica: {}".format(bin(user)))

elif op == 2:
    print("\033[30;m Seu valor em octal fica: {}".format(oct(user)))


elif op == 3:
    print("\033[30;m Seu valor em hexadecimal fica: {}".format(hex(user)))

else:
    print("\033[32;41;m Opção invalido!\033[m")

#end