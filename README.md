  
# 0x00. AirBnB clone - The console
Airbnb is a full-stack web application that includes database storage, a back-end API and front-end interface.  
This is the first step/edition towards building this full web application. The goal is to create a command interpreter for the Airbnb objects. this also serves as a debugging tool for the programmer/command handler because it is an interactive console that provides you with a quick way to create your data model, manage (create, update, destroy, etc) objects via a console / command interpreter, store and persist objects to a file (JSON file), and also to execute commands and try out or test codes without creating a file.  
##### This first part of the project is crucial and also the building block where the HTML/CSS templating, database storage, API, and front-end interface will be integrated.  
## Concepts Employed In This Project:  
* Managing your custom Modules as python packages -> [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
* Line oriented comand interpreters -> [Cmd Module](https://docs.python.org/3.8/library/cmd.html#module-cmd)  
* Generating Random Id(s) with Universal unique identifier -> [Uuid module](https://docs.python.org/3.8/library/uuid.html#module-uuid)  
* Parking and unparcking of arguments -> [*args & **kwargs]()
* Converting objects to byte stream & reconstructing them back from byte stream -> [Serialization & deserialization](https://docs.python.org/3/library/json.html#module-json)  
* Implementtation of Date and time -> [Datetime module](https://docs.python.org/3.8/library/datetime.html#module-datetime)
### Testing  
* Used python Unittesting -> [Python Unittest](https://realpython.com/python-testing/)
### How to start and use this command interpreter:
* Clone this repository -> `git clone https://github.com/El-gibbor/AirBnB_clone.git`  
* Access the directory -> `cd AirBnB_clone`  
* Run the console application interactively:  
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```  
* Or, You can also run it non interactively:   
```
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
```  
### Authors:
* Ojore Chris -> [Linkdin](https://www.linkedin.com/in/ojore-chris/) | [Github](https://github.com/creasedigital) | [Portfolio](https://creasedigital.github.io/) | [Twitter](https://twitter.com/creasedigital)  
* Chiagoziem Elgibbor -> [Linkdin](https://www.linkedin.com/in/chiagoziem-elgibbor-173858208/) | [Twitter](https://twitter.com/Chiagoziem94)
