import random

i=1
user_gana = 0
computer_gana = 0

while i<4:
  print("RONDA {}" .format(i))
  user_option = input("piedra, papel o tijera: ")
  options = ("piedra", "papel", "tijera")
  computer_option = random.choice(options)
  print("el computador eligio: {}".format(computer_option))
  
  if user_option == computer_option:
    print("empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("ganaste")
      user_gana += 1
    else:
      print("perdiste")
      computer_gana += 1
  elif user_option == "papel":
    if computer_option == "tijera":
      print("perdiste")
      computer_gana += 1
    else:
      print("ganaste")
      user_gana += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("ganaste")
      user_gana += 1
    else:
      print("perdiste")
      computer_gana += 1
  else:
    print("opción incorrecta")

  print("****"*10)

  i+=1

if user_gana > computer_gana:
  print("el ganador es user")
else:
  print("el ganador es computer")
