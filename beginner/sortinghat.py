#our variables to count the score towards each house
gryffindorScore=0
ravenclawScore=0
hufflepuffScore=0
slytherinScore=0

#our total score counter
totalScore= gryffindorScore+ ravenclawScore+ hufflepuffScore+ slytherinScore

#an intro
print("Welcome to Hogwarts School of Witchcraft and Wizardry.")
print("\nWe have four houses here at Hogwarts: \nGryffindor, Ravenclaw, Hufflepuff, and Slytherin. \n\nI'm sure you're wondering \"How do we know which house each of our students belong to?\"")
print("We have the infamous sorting hat, which will just ask you a couple questions and designate your house.")

#question1
print("\nQ1) Do you like Dawn or Dusk?\n    1) Dawn \n    2) Dusk")

answer=int(input("Enter your selection here: "))

if answer==1:
    gryffindorScore +=1
    ravenclawScore +=1
elif answer==2:
    hufflepuffScore +=1
    slytherinScore +=1
else:
    print("Wrong input.")

#question 2  
print("\nQ2) When I'm dead, I want people to remember me as: \n    1) The Good \n    2) The Great \n    3) The Wise \n    4)The Bold")
answer=int(input("Enter your selection here: "))

if answer==1:
    hufflepuffScore +=2
elif answer==2:
    slytherinScore +=2
elif answer==3:
    ravenclawScore +=2
elif answer==4:
    gryffindorScore +=2
else:
    print("Wrong input.")   

#question 3
print("\nQ3) Which kind of instrument most pleases your ear? \n    1)The violin \n    2)The trumpet \n    3)The piano \n    4)The drum")
answer=int(input("Enter your selection here: "))


if answer==1:
    slytherinScore +=4
elif answer==2:
    hufflepuffScore +=4
elif answer==3:
    ravenclawScore +=4
elif answer==4:
    gryffindorScore +=4
else:
    print("Wrong input")
    
#print the total points for each house
print("Gryffindor: ", gryffindorScore)
print("Ravenclaw: " , ravenclawScore)
print("Hufflepuff: " , hufflepuffScore)
print("Slytherin: " , slytherinScore)

#can do the print statements in one single line of code:
#print("\nGryffindor: ", gryffindorScore , "\nRavenclaw: " , ravenclawScore , "\nHufflepuff: " , hufflepuffScore , "\nSlytherin: " , slytherinScore)

    
#calculating the house with the most points!
if (gryffindorScore>ravenclawScore and gryffindorScore>hufflepuffScore and gryffindorScore>slytherinScore):
    print("\nGRYFFINDOR!! 🦁")
elif(ravenclawScore>gryffindorScore and ravenclawScore>hufflepuffScore and ravenclawScore>slytherinScore):
    print("\nRAVENCLAW!! 🦅")
elif(hufflepuffScore>gryffindorScore and hufflepuffScore>ravenclawScore and hufflepuffScore>slytherinScore):
    print("\nHUFFLEPUFF!! 🦡")
else:
    print("\nSLYTHERIN!! 🐍")