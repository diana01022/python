# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
# (paarisarvu mõiste - odd/even)
num = int(input("5:"))
if (num % 2 ) == 0:
    print("{0} is Even".format(num)) 
else:
    print("{0} is Odd".format(num))