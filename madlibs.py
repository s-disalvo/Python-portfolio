# string concatenation (aka how to put stings together)
#suppose we want to create a string that says "subscribe to ___"
# youtuber = "Kylie Ying" # some string varible

# a few ways to do this 
# print ("subscribe to" + youtuber)
# print ("subscribe to {}" + .format(youtuber))
# print (f"subscribe to + {youtuber}")

# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

# madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
# I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# print(madlib)

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
verb1 = input("Verb: ")
place = input("Place: ")
adj3 = input("Adjective: ")
animal = input("Animal: ")
adj4 = input("Adjective: ")
name = input("Name: ")
famous_person = input("Famous Person: ")
verb2 = input("Verb: ")
adj5 = input("Adjective: ")

madlib = f"Cats are {adj1} pets to have. They can do so many things. The most {adj2} thing they can do is {verb1}! One time, I saw my cat at \
{place} and he was acting like a {adj3} {animal}. Cats ought to have {adj4} names as well, such as {name}. That's the name of \
{famous_person}'s cat. So {verb2} on over to your local pet shelter and pick up your new {adj5} friend!"

print(madlib)