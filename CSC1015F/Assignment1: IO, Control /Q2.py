# spam
# Shingirai Maburutse
# 08/01/21

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
money30 = money*0.3

print("Dearest " ,first_name, "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk ",last_name," your long lost relative from Mapsfostol.\nMy father left the sum of ", money,"  USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in ", country, sep="", end=".")
print("I desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - ",money30,"USD,\nfor your help. Please get in touch with me at this email address asap.\nYours sincerely\nFrank ",last_name, sep="")
