0x00. AirBnB clone - The console
Description of the project.
The Airbnb Clone: The console. This repository holds a command interpreter and classes (such as; BaseModel classand other classes that inherit from BaseModel: Amenity, City, State, Place, Review), and a command interpreterlike a shell



Command interpreter functionalities.
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
File Storage Engine:
/models/engine/file_storage.py
Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: ``$ echo "python3 -m unittest discover tests" | bash```
**Authors**
1. Makoha Dharren Pius
2. Haruna Danladi Maina DANLADI

