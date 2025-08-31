
print("Welcome to Mad Libs! 🎉")
print("Please provide words as asked. Let's make a funny story!\n")


adjective1 = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
place = input("Enter a place: ")
adjective2 = input("Enter another adjective: ")
food = input("Enter a type of food: ")
verb2 = input("Enter another verb: ")
friend_name = input("Enter a friend's name: ")
object_name = input("Enter an object: ")

story = f"""
One {adjective1} morning, I woke up and found a {animal} in my room!  
It started to {verb1} around like it owned the place.  
So, I decided to take it to {place}, hoping someone there would help.  

But instead, people just laughed because the {animal} was wearing a {adjective2} hat  
and eating {food} noisily.  

Suddenly, it began to {verb2} on top of a {object_name},  
and everyone, including my best friend {friend_name}, joined in the fun.  

That day was the most unforgettable adventure of my life!
"""

# Print the funny story
print("\nHere's your Mad Libs story:")
print(story)
