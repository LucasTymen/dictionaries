"""

Creating Dictionaries
Make a Dictionary

In the previous exercise, we saw a dictionary that maps strings to numbers (i.e., "avocado toast": 6). However, the keys
can be numbers as well.

For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:
"""
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
"""
Values can be of any type. We can use a string, a number, a list, or even another dictionary as the value associated
with a key!

For example:
"""
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
"""
The list ["Aaron", "Delila", "Samson"], which is the value for the key "software design", represents the students in
that class.

We can also mix and match key and value types. For example:
"""
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
"""
Instructions
1.

Create a dictionary called translations that maps the following words in English to their definitions in Sindarin (the
language of the elves):
English 	Sindarin
mountain 	orod
bread 	bass
friend 	mellon
horse 	roch

It should look something like:

translations = {"mountain": "orod", "bread": "bass", ...}

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Does a dictionary have to be created with initial values?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
