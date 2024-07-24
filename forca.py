palavra = input("Digite a palavra secreta: ")

desenhos = ['''
 +---+
 |   |
     |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========''']

cont = 0

print(desenhos[cont])
print()

for i in range(len(palavra)):
    print('_',end=" ")
print()

pal = []
for i in range(len(palavra)):
    pal.append('_')
while(cont<6):
    igual = True
    letra = input(("Digite uma letra: "))     

    if letra in palavra:
        print(desenhos[cont])
        print()
        for i in range(len(palavra)):
            if letra == palavra[i]:
                print(letra, end=" ")
                pal[i] = palavra[i]
            else:
                if pal[i] != '_':
                    print(pal[i],end=" ")
                    
                else:
                    print("_",end=" ")
        print()

    else:
        cont += 1
        print(desenhos[cont])
        print()  
        for i in range(len(palavra)):
            if letra == palavra[i]:
                print(letra, end=" ")
                pal[i] = palavra[i]
            else:
                if pal[i] != '_':
                    print(pal[i],end=" ")
                    
                else:
                    print("_",end=" ")
        print()

    for i in range(len(palavra)):
        if pal[i] != palavra[i]:
            igual = False

    if igual == True:
        break

if(cont == 6):
    print("Voce teve muitas oportunidades e perdeu!")

else:
    print(f'Sim! A palavra secreta eh "{palavra}"')