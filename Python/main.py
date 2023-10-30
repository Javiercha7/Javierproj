Option1 = "yes"
Option2 = "no"
total = 0
total2 = 0
q1 = "Would You rather eat a Hawaian pizza or a Meatza? "
# Question used for the user
q2 = "Would You rather Go "
#

def userYes():
  global total 
  total = total + 1
  print(f"Really me too!! Is the best pizza out there and is not debatable {total}")  
  # Add a total variable and displayis how many people aggre with your decision.

def userNo():
  global total2
  total2 = total + 1
  print(f"Ohh nicee choice, could be better though {total2}")
  # Add a total variable and displayis how many people aggre with your decision.


responce1 = input(q1)
# gets the data from the user in the program

if responce1[0].lower() == "h":
   userYes()
# if the user answers wth a word that has a lowercase y in the beginning, it would print the total and a funny message
  
elif responce1[0].lower() == "m":
  userNo()
# if the user answers wth a word that has a lowercase n in the beginning, it would print the total and a funny message
  


# if user == "Yes":
#  userYes()
# elif user == "No":
#   userNo()
  
