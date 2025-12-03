# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). 
# (loogikatehted - logic operators)
# test

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(a, b, c)
if a > b and a > c:
    print("a is maximum") 

elif b > c:
    print("b is maximum")
    
else:
    print("c is maximum")