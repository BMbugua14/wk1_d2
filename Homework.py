#Task1
#place = input("Choose a place: forest or cave? ")

#if place = "forest":
    #action = input("climb a tree or cross a river?")
    #if action = "climb a tree":
        #print("You found a bird's nest!")
    #else action = "cross a river":
        #print("You found a boat!")
#elif place = "cave":
    #print("You find a hidden treasure!")

#Answer1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#Answer2
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark")
    if action == "light a torch":
        print("You discovered a hidden path")
    elif action == "proceed in the dark":
        print("Beware of goblins & slimes")

#Answer3
c_state = "focused"
if c_state == "tired":
    pass
if c_state == "hungry":
    pass
else:
    print("I should code before i go to bed")

#Task2
#attendees = input("Enter number of attendees: ")
#venue = "large hall" if attendees > 100 elif "conference room"
#print(venue)

#Answer1

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"    
print(venue) 

#Answer2
eats = input("What should we eat?")
if  eats == "vegetarian":
    print("Lets go for Veggie Delight Caterers")
else:
    print("Lets go for Gourmet Meals Caterers")
print(eats)