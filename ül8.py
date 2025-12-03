# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.
year=int(input("2020:"))
if (year % 400 == 0) or (year % 4 == 0
and year != 0):
  print("The year is a leap year.")
elif year % 2 == 0:
  print("The year is even but not a leap year.")   
else:
  print("The year is not a leap year and not even.")  
