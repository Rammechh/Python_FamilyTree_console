from collections import defaultdict

class FamilyTree:

    def __init__(self):
        self.displayMenuOptions()

    def  displayMenuOptions(self):

        print("Kindly input atleast one person name to continue")
        personName = input().upper()
        #Singleton
        p = Person(personName)

        while(True):
        
            print("************************* Family Tree *************************")
            print("1. Add Person")
            print("2. Add Relationship")
            print("3. Get Relationship")
            print("4. Count of Sons")
            print("5. Count of Daughter")
            print("6. Count of wives")
            print("7. Show all Family members")
            print("8. Quit")

            #Get Above Option
            print("Enter option from 1-8")
            option = int(input())

            if option == 1:
                print("Input Person name")
                personName = input().upper()
                p.addPerson(personName)
            
            if option == 2:
               
                print("Enter name1(Parent or Male Partner) and name2(Child or Female Partner) to be connected")
                while(True):
                    name1 = input().upper()
                    if name1 not in p.persons:
                        print("Entered name1 not available")
                        break
                    name2 = input().upper()
                    if name2 not in p.persons:
                        print("Entered name2 not available")
                        break

                    print("Enter the Relationship\n1.Son\n2.Daughter\n3.Partner")
                    relation = int(input())
                    p.Relationship(name1, name2, relation)
                    break
            
            if option == 3:
                p.getAllFamilyMembers()
                print("Enter name1 and name2 to be get relationship")
                while(True):
                    name1 = input().upper()
                    if name1 not in p.persons:
                        print("Entered name1 not available")
                        break
                    name2 = input().upper()
                    if name2 not in p.persons:
                        print("Entered name2 not available")
                        break

                    p.getRelationship(name1, name2)
                    break            

            if option == 4:
                p.getAllFamilyMembers()
                print("Enter Parent name")
                parent = input().upper()
                if parent not in p.persons:
                    print("Person not available in Family")
                else:
                    p.getSonCount(parent)
            
            if option == 5:
                p.getAllFamilyMembers()
                print("Enter Parent name")
                parent = input().upper()
                if parent not in p.persons:
                    print("Person not available in Family")
                else:
                    p.getDaughterCount(parent)
            
            if option == 6:
                p.getAllFamilyMembers()
                print("Enter Partner name")
                partner = input().upper()
                if partner not in p.persons:
                    print("Person not available in Family")
                else:
                    p.getWifeCount(partner)
            
            if option == 7:
                p.getAllFamilyMembers()

            if option == 8:
                break
            
            
            
class Person:

    #All Family members
    #Avoiding Duplicates (Not real life scenario)
    persons = set()

    #Relationships
    relations_son = defaultdict(list)
    relations_daughter = defaultdict(list)
    relations_wife = defaultdict(list)

    def __init__(self, name):
        self.name = name
        self.addPerson(name)

    def addPerson(self,name):
        self.persons.add(name)

    def getAllFamilyMembers(self):
        print(f'All Family members: {self.persons}')

    # getter method
    def getname(self):
        return self.name

    #Add Relationship
    def Relationship(self, name1, name2, rel):
        if rel == 1:
            self.relations_son[name1].append(name2)
            print(f'{self.relations_son[name1]}  is son of  {name1}')

        if rel == 2:
            self.relations_daughter[name1].append(name2)
            print(f'{self.relations_daughter[name1]}  is daughter of  {name1}')

        if rel == 3:
            self.relations_wife[name1].append(name2)
            print(f'{self.relations_wife[name1]}  is wife of  {name1}')
    
    #Son Count
    def getSonCount(self, name):
        if name in self.relations_son:
            print(f'Son count {len(self.relations_son[name])}')
        else:
            print("Son Count : 0")

    #Daughter Count
    def getDaughterCount(self, name):
        if name in self.relations_daughter:
            print(f'Daughter count {len(self.relations_daughter[name])}')
        else:
            print("Daughter Count : 0")
    
    # Wife Count
    def getWifeCount(self, name):
        if name in self.relations_wife:
            print(f'Wife count {len(self.relations_wife[name])}')
        else:
            print("Relation not available")
    
    #Get Raltionship
    def getRelationship(self, name1, name2):
        #Check name2 is son of name1
        if name1 in self.relations_son:
            if name2 in self.relations_son[name1]:
                print(f'{name2} is son of {name1}')
        
        #Check name1 is son of name2
        elif name2 in self.relations_son:
            if name1 in self.relations_son[name2]:
                print(f'{name1} is son of {name2}')
        
        #Check name2 is Daughter of name1
        elif name1 in self.relations_daughter:
            if name2 in self.relations_daughter[name1]:
                print(f'{name2} is daughter of {name1}')
        
        #Check name1 is Daughter of name2
        elif name2 in self.relations_daughter:
            if name1 in self.relations_daughter[name2]:
                print(f'{name1} is daughter of {name2}')
        
        #Check name2 is wife of name1
        elif name1 in self.relations_wife:
            if name2 in self.relations_wife[name1]:
                print(f'{name2} is wife of {name1}')

        #Check name1 is wife of name2
        elif name2 in self.relations_wife:
            if name1 in self.relations_wife[name2]:
                print(f'{name1} is wife of {name2}')

        else:
            print("No Relationship")
            
if __name__ == "__main__":
    FamilyTree()

