class Node:
    def __init__(self, data):
        self.data=data #Något värde
        self.next=None  # En pekare till nästa nod


class LinkedQ:
    def __init__(self):
        self.__first= None
        self.__last= None

    #1.göra en tom lista
    #2.gör en if/else sats
    #-ifall den är tom, skapa en nod som både first och last pekar på
    #-ifall den inte är tom måste "last" pekaren ändras från sig själv till den sista noden
    #och placera den nya noden sist
    def enqueue(self,kort):
        nynod=Node(kort)   #Gör en ny nod från classen Node
        if self.__first==None:
            self.__first=nynod
            self.__last=self.__first   #Då den första noden är dessamma som den sista
    
    #Ifall det redan finns Noder så startar else:
        else:
            self.__last.next=nynod  #Gör så att den sista nodens next pekare hamnar på vår nya nod
            self.__last=nynod       #Gör så att "last" pekaren pekar på når nya tillagda nod


    #spara den första noden till en variabel
    #flytta sedan fram den andra noden så att det blir den första
    def dequeue(self):
        poppadnod=self.__first.data
        self.__first=self.__first.next
        return poppadnod

    # Metod för att kolla om "first" pekaren pekar på något, isåfall returnas "false" och det betyder då
    #att det finns någon nod kvar i programet
    def isEmpty(self): 
        if self.__first:
            return False
        elif not self.__first:
            return True