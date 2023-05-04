"""

Creating Dictionaries
Review

So far we have learned:

    How to create a dictionary
    How to add elements to a dictionary
    How to update elements in a dictionary
    How to use a dict comprehension to create a dictionary from two lists

Let’s practice these skills!
Instructions
1.

We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the
amount of times each song has been played.

Using a dict comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a
song:playcount pair for each song in songs and each playcount in playcounts.

To create a dictionary from a dict comprehension use this syntax:

new_dict = {key:value for key, value in zip(key_list, value_list)}

2.

Print plays.
3.

After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.
4.

This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to
be 94 in the plays dictionary.
5.

Create a dictionary called library that has two key: value pairs:

    key "The Best Songs" with a value of plays, the dictionary you created
    key "Sunday Feelings" with a value of an empty dictionary

6.

Print library.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""
