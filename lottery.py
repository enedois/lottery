import math, random
mynumbers = []


def get6numbers():
    allnumbers = []
    ##for loop to generate 6 random numbers
    for i in range(1,61):
        allnumbers.append(i)
        random.shuffle(allnumbers)
        
    return (allnumbers[0:6])



mynumbers = (get6numbers())
print("Meus Numeros" +str(mynumbers))

won = False
tentativas = 0
maxacertos=0;

while not won:
    tentativas+=1;
    sorteio =  get6numbers();
    acertos = list(set(mynumbers).intersection(sorteio))
    
    if len(acertos) == 6:
        ##print("Ganhei")
        won = True
        print("GANHEI!! Tentativas:"+str(tentativas)+"|"+str(mynumbers)+"|"+str(sorteio)+"|"+"Acertos:"+str(len(acertos)))
        
    else:
        ##print("Não ganhei")
        ##print(len(acertos))
        if(len(acertos)>=maxacertos):
            maxacertos=len(acertos)
            print("Tentativas:"+str(tentativas)+"|"+str(mynumbers)+"|"+str(sorteio)+"|"+"Acertos:"+str(len(acertos)))
            won = False;
        won = False;
        ##print("Tentativas:"+str(tentativas)+"|"+str(mynumbers)+"|"+str(sorteio)+"|"+"Acertos:"+str(len(acertos)))


    




    







