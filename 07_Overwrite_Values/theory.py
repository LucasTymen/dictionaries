"""

Creating Dictionaries
Overwrite Values

We know that we can add a key by using the following syntax:
"""
menu["banana"] = 3
"""
This will create a key "banana" and set its value to 3. But what if we used a key that already has an entry in the menu
dictionary?

In that case, our value assignment would overwrite the existing value attached to that key. We can overwrite the value
of "oatmeal" like this:
"""
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
"""
This would yield:

{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

Notice the value of "oatmeal" has now changed to 5.
Instructions
1.

Add the key "Supporting Actress" and set the value to "Viola Davis".
2.

Without changing the definition of the dictionary oscar_winners, change the value associated with the key "Best Picture"
to "Moonlight".
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
