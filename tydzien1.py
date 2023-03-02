from collections import deque

class zadanie1:
    
    
    def count_netto_price (brutto_price, podatek):
        roznica = brutto_price * podatek
        netto_price = brutto_price - roznica
        return netto_price
    
    def kolejka ():
        queue = deque(["Eric", "John", "Michael"])
        pass
    
    def to_file(x):
        x = str(x) + "\n"
        with open ("plik.txt", "w") as file:
            file.write(x)
            
    
class zajecia:
    studenci = []
    
    def zapisz_studenta(name, surname):
        student= str(name) + str(surname)
        studenci += student
    
    def ilosc_studentow():
        return len(studenci)
    
    def ilość_studentow():
        if ilosc > 10:
            print ("Za duzo osob zapisanych na zajecia")
        elif len( studenci) < 0:
            print("Błędna ilosć studentów zapisanych")
        else:
            x = zapisz_studenta()
            
            
        
            
            