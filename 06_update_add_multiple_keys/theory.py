"""
Creating Dictionaries
Add Multiple Keys

If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

Looking at our sensors object from a previous exercise:
"""
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
"""
If we wanted to add 3 new rooms, we could use:
"""
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
"""
This would add all three items to the sensors dictionary.

Now, sensors looks like:

{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

Instructions
1.

In one line of code, add two new users to the user_ids dictionary:

    theLooper, with an id of 138475
    stringQueen, with an id of 85739

It should look something like:
"""
user_ids.update({"username1": 100, "username2": 101})
"""
2.

Print user_ids.

It should look something like:
"""
print(name)
"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
