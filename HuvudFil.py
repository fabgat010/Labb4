from bintreeFile import Bintree
from linkedQFile import LinkedQ


gamla= Bintree()
ordlistan = Bintree()
q=LinkedQ()
class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

class Klar(Exception):
    def __init__ (self):
        pass
    
#1.byta ut varje bokstav i startordet. Sedan ska ordet jämföras
#med ordlistan(svenska) för att se vilka ord som finns med. Ifall den finns med ska den även jämföra 
#listan gamla och ifall den finns i ordlistan men inte i gamla ska den printar den ordet och lägger till
# i gamla 
def makechildren(startord,slutord):
    alfabetet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
    for i in range(len(alfabetet)):
            förstabokstav= alfabetet[(i)] + startord[1] + startord[2]
            if förstabokstav in ordlistan:
                if förstabokstav not in gamla:
                    gamla.put(förstabokstav)
                    #print(förstabokstav)
                    q.enqueue(förstabokstav)
                    if förstabokstav == slutord:						
                            raise Klar
                

            andrabokstav= startord[0]+ alfabetet[i]+ startord[2]
            if andrabokstav in ordlistan:
                if andrabokstav not in gamla:
                    gamla.put(andrabokstav)
                    #print(andrabokstav)
                    q.enqueue(andrabokstav)
                    if andrabokstav ==slutord:						
                            raise Klar

            tredjebokstav= startord[0] + startord[1] + alfabetet[i]
            if tredjebokstav in ordlistan:
                if tredjebokstav not in gamla:
                    gamla.put(tredjebokstav)
                    #print(tredjebokstav)
                    q.enqueue(tredjebokstav)
                    if tredjebokstav == slutord:						
                            raise Klar
                    



def main():
    with open("/Users/Fabian/Documents/DataOptimering/Labb4/word3.txt", "r", encoding = "utf-8") as ordfil:
        for rad in ordfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet not in ordlistan:
                ordlistan.put(ordet)           # in i sökträdet
    
    #start_ord=input("Välj ditt startord: ")
    #slutord= input("välj ditt slutord: ")
    start_ord="söt"
    slutord= "sur"
    q.enqueue(start_ord)
    try:
        while not q.isEmpty():
            nod = q.dequeue()
            makechildren(nod,slutord)
        print("Det finns tyvär ingen väg")
    except Klar:
        print("Det finns en väg för", start_ord, "till", slutord)

main()



