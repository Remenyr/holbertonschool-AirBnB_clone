# Project name: AirBnB clone

## First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## What's a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Learning Objectives
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## How to Use Command Interpreter

|Commands   |Sample Usage   |Functionality   |
| ------------ | ------------ | ------------ |
|help   |help   |displays all commands available   |
|create   |create < class>  |creates new object (ex. a new User, Place)   |
|update   |User.update('427', {'name' : 'Leo_n_Juan'})   |updates attribute of an object   |
|destroy   | User.destroy('427')  |destroys specified object   |
|show   |User.show('427')   |	retrieve an object from a file, a database   |
|all   |User.all()   |display all objects in class  |
|count   |User.count()   |returns count of objects in specified class   |
|quit   |quit   |exits   |

## Installation
git clone https://github.com/cestrad5/holbertonschool-AirBnB_clone.git<br>
cd holbertonschool-AirBnB_clone

## Usage

**Interactive Mode**

$ ./console.py<br>
(hbnb) help<br>

##### ###### Documented commands (type help <topic>):
========================================<br>
EOF  help  quit<br>

(hbnb)<br>
(hbnb)<br>
(hbnb) quit<br>
$<br>

**Non-Interactive Mode**

$ echo "help" | ./console.py<br>
(hbnb)<br>

##### ###### DOCUMENTED COMMANDS (TYPE HELP <TOPIC>):
========================================<br>
EOF  help  quit<br>
(hbnb)<br>
$<br>
$ cat test_help<br>
help<br>
$<br>
$ cat test_help | ./console.py<br>
(hbnb)<br>

##### ###### Documented commands (type help <topic>):
========================================<br>
EOF  help  quit<br>
(hbnb)<br>
$<br>

## Files

| File Name  |  Description |
| ------------ | ------------ |
|[README.md](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/README.md "README.md")   |	A description of the Holberton AirBnB Project   |
|[AUTHORS](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/AUTHORS "AUTHORS")  |A listing of the project contributors   |
|[console.py](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/console.py "console.py")   |The program to launch the HBNB console   |
|[basemodel.py](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/base_model.py "basemodel.py")   |Defines the BaseModel Class   |
|[user.py ](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/user.py "user.py ")  |Defines the User Class, a subclass of BaseModel   |
|[file.storage.py ](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py "file.storage.py ") | Defines the FileStorage Class & handles the database  |
|[city.py](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/city.py "city.py")   |	Defines the City Class, a subclass of BaseModel   |
|[state.py](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/state.py "state.py")   |	Defines the User Class, a subclass of BaseModel   |
|[amenity.py](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/amenity.py "amenity.py")   |Defines the Amenity Class, a subclass of BaseModel   |
|[review.py](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/review.py "review.py")   |Defines the Review Class, a subclass of BaseModel   |
|[place.py](https://github.com/cestrad5/holbertonschool-AirBnB_clone/blob/main/models/place.py "place.py")   |	Defines the Place Class, a subclass of BaseModel   |
|[tests](https://github.com/cestrad5/holbertonschool-AirBnB_clone/tree/main/tests "tests")   |	The test directory containing the unittest files for each Class   |

## Authors
- Camilo Estrada - <cestrad5@gmail.com>
- Luis Alejandro Puerta - <puertaalejo02@gmail.com>