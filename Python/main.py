Option1 = "yes"
Option2 = "no"
count = 0
total = 0
total2 = 0
Questions = ["Would You rather eat a Hawaian pizza or a Meatza? ", 
              "Would You rather Go Chernobyl or North  Korea","Nothing"]
# Question used for the user


# q1 = "Would You rather eat a Hawaian pizza or a Meatza? "
# # Question used for the user

# q2 = "Would You rather Go Chernobyl or North  Korea"
# # Question used for the user



def userYes():
  global total 
  total = total + 1
  if total == 1 :
    print(f"Really me too!! Is the best pizza out there and is not debatable \nThis many people support this option {total}")  
  else :
       print(f"You may gain superpowers like Homelander or just die but hey better than being in North Korea \nThis many people support this option {total}")
  # Add a total variable and displayis how many people aggre with your decision.



def userNo():
  global total2
  total2 = total2 + 1
  if  total2 == 1 :
    print(f"Ohh nicee choice, could be better though \nThis many people support this option {total2}")
  else :
       print(f"Say bye bye to your freedom! say hello to your forced marriage and getting exploit labor wise. \nThis many people support this option {total2}")
 
  # Add a total variable and display is how many people aggre with your decision.


while count < 2 :
    print(f'Select either yes(1) or no(2)')
    responce1 = int(input(Questions[0]))
    if responce1 == 1:
        userYes()
    else :
        userNo()
    
    del Questions[0]
count+= 1
# gets the data from the user in the program  

