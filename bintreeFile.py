#Labb 3 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __gt__(self,other): #För att inte få typeerror > ( mellan node och int)
        return 0

    def __str__(self):
	    return self.data 


class Bintree:
    def __init__(self, root=None):
        self.root = root

    def put(self,newvalue):
        if self.root == None:
            self.root = Node(newvalue)
        else:
            self.putta(self.root,newvalue)
    
    def __lt__(self,other):
        return 0

    def __contains__(self ,value):
        # True om value finns i trädet, False annars
        if self.root is not None:
            return self.finns(self.root,value)
        else:
            return False
       
    def write(self):
        # Skriver ut trädet i inorder
        self.skriv(self.root)
        print("\n")

    #Startar i roten och jobbar sig ner genom trädet för att hitta ett tal/ord
    #Använder sig av samma princip som att lägga till i ett träd och vid varje Nod så kontrlllerar
    #Den ifall det är vad man söker om, om de e falskt så går den vidare genom att använda > < för att hitta vidare.
    def finns(self ,p,data):
        while p is not None:
            if data==p.data:
                return True
            elif data < p.data:
               return self.finns(p.left, data) 
            elif data > p.data: 
                return self.finns(p.right, data) 
            else:
                return False    
    #är funktionen som jämför ifall värdet som skickades
    # in är större eller mindre än den befintliga roten.
    # ifall det finns flera "Barn" till roten så fortsätter man loopa def putta() tills dess att man
    #har kommit längst ner i trädet och hittat en plats åt "value"
    def putta(self, x_value , value ):
        if value < x_value.data:
            if x_value.left == None:
                x_value.left = Node(value) 
            else:
                self.putta(x_value.left,value)
        if value > x_value.data:
            if x_value.right == None:
                x_value.right = Node(value)
            else:
                self.putta(x_value.right,value)


#Går längst ner till vänster tills att left-pekaren pekar på none, då printar den noden, sen går den till right och gör samma sak.
#repeterar den tills den gått igenom hela trädet, från vänster till höger.
    def skriv(self,p):
        if p is not None:
            self.skriv(p.left)
            print(p.data)
            self.skriv(p.right)


#Test kod för att testa trädet
""" tree = Bintree()
tree.put("2")
tree.put("1")
tree.put("3")
print ("1" in tree)
tree.write()

__contains__ """