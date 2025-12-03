# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks.
#  Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi.
#  Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida.
#  Külje pikkused ei pea olema täisarvud.
#  (ujukomaarv - float)
a = float(input("5:"))
b = float(input("8:"))
c = float(input("9:"))
 
if(a + b > c) and ( a + c > b) and ( b + c > a):

 if a == b == c:
   print("The triangle is equilateral.")
elif a == b or b == c or a == c: 
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

else:
    print("A triangle with those side lenghts cannot exist.")