# AirBnB_clone - Console ⛪
A full-stack web application that includes database storage, a back-end API and a front-end interface.  
This console is our initial step in creating a full-stack web application. At its core, it acts as a command interpreter for Airbnb objects, enabling one to interactively manipulate data models, manage objects, and execute commands.

## Key Features:  
- **Data Modeling:** Design our data model effortlessly.  
- **Interactive Management**: Create objects, update, destroy, and more, all within the console.   
- **Persistent Storage:** Store and persist objects seamlessly to a JSON file.  
- **Seamless Abstraction:** Implemented a storage engine that abstracts complexities. You focus on your objects, not storage intricacies!
    - _With this storage system, one won’t worry about the nitty-gritty details of object storage. Whether you're coding in the console, crafting the front-end, or building the RestAPI, the storage abstraction ensures consistency and flexibility. Storage type can be easily switched without rewriting the entire codebase._  
## Why it Matters: 💥 
This console serves as the foundation, where HTML/CSS templating, database storage, API, and the front-end interface will merge seamlessly. It’s a debugging tool, our code testing ground, and our data model creator.  
## Concepts Employed in this Project:  
- [Packages](https://docs.python.org/3.4/tutorial/modules.html#packages) - **Managing Modules as Packages:** Organize custom modules as Python packages.  
- [Cmd Module](https://docs.python.org/3.8/library/cmd.html#module-cmd) - Leveraging the Cmd Module for efficient command handling.  
- [UUID Module](https://docs.python.org/3.8/library/uuid.html#module-uuid) - Utilized the Universal Unique Identifier (UUID) module for generating random IDs.  
- [Args and Kwargs](https://www.scaler.com/topics/python/args-and-kwargs-in-python/) - Mastered `*args` and `**kwargs` for versatile argument handling.  
- [JSON](https://docs.python.org/3/library/json.html#module-json) - Converting objects to byte streams and reconstructing them using serialization and deserialization.  
- [Datetime Module](https://docs.python.org/3.8/library/datetime.html#module-datetime) - Employed the Datetime module for effective date and time handling.
- [Unit Test](https://realpython.com/python-testing/) - Test Driven Devolopment.
## How This Console App Works  
### Interactively ⤵️
```
ubuntu@elgibbor~$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
ubuntu@elgibbor~$
```
### None Interactively ⤵️  
```
ubuntu@elgibbor~$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
ubuntu@elgibbor~$
ubuntu@elgibbor~$ cat test_help
help
ubuntu@elgibbor~$
ubuntu@elgibbor~$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
ubuntu@elgibbo~$
```
## Authors: 🧠  
Manny Quansah (IamDeadalus) - [Github](https://github.com/IamDaedalus?tab=repositories) | [Twitter](https://twitter.com/daedalus_here)  
Chiagoziem El-gibbor - [Twitter](https://twitter.com/Chi_Elgibbor) | [LinkedIn](https://www.linkedin.com/in/elgibbor/) | [Blog](https://hashnode.com/@Elgibbor)
