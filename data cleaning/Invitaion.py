# The Scenario: You are making a list of friends to invite to a party, but you have had a fight with "Omkar". 
# You want to print the invite for everyone EXCEPT him.

# input
friends = ["Rohit", "Omkar", "Shagun", "Parth"]

# for loop for entry one by one 
for name in friends:

    # if the omkar found then continue will skip the omkar and continue the invitaion
    if name == 'Omkar':
        print("Skipping Omkar...")
        continue
    else:
        print(f"Sending invitation to: {name}")