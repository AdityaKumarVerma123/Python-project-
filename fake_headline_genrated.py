#fack headline genrator using a python code .


import random 
subjects = [
    "sharuk khan",
    "salman khan",
    "modi ji ",
    "A mumbai cat",
    "Agroup of monkeys",
    "virat kohli",
    "auto rikshaw driver from delhi"
]

actions =[
    "lunches",
    "cancels",
    "dances with",
    "eats",
    "decleares",
    "orders",
    "celebrates"
]

place_or_think= [
    "at red fort",
    "in mubai local train",
    "a plote of samosa",
    "inside parliament",
    "during IPL match",
    "at india gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_think)

    headline = f"BREAKING NEWS:-{subject} {action} {place_or_thing}"
    print("\n"+headline)

    user_input = input("\nDo you want another headline? (yes/no):-").strip().lower()

    if user_input == "no":
        break


print("\nThank you for using the fake headline generator. Goodbye!")    
    