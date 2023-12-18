Michael Hecox
Student ID # 00243521
Course # CIS-153-L8
Final Project
Readme and other general documentation

a simple text adventure game where you explore a series of rooms and collect items

to play the game, simply run the python script while ensuring that the layout.txt file is in the same directory.

valid inputs at this time are:

turn (left, right. cardinal directions become available after finding the compass)

move (forward, left, right, cardinal directions become available after finding the compass)

take (item on ground)

drop (item in inventory)

inventory

look

exit/quit

the only necessary library to import is regular expressions

the only python functionality I used which was not taught in the course was eval(), which I read up on at https://www.tutorialspoint.com/How-to-convert-a-String-representation-of-a-Dictionary-to-a-dictionary-in-Python
this was used to compactly convert text read from the load file into dictionaries

categories used:

variables
if statements
functions (abstractions, parameters, return values)
for/while loops
conditional loop
lists and dictionaries
string manipulation
files
regular expressions

future work: at some point I would like to add proper saving and loading, as well as the ability to actually use items, and some sort of win condition.
saving and loading should be relatively simple to add, and would share a lot of code with the existing loadNew function, they were purely cut for time. the other functionality would require some additional work which I have yet to figure out fully.

