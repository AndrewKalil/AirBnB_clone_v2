<center > <h1 > HBNB - The Console </center >

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center > <h3 > Repository Contents by Project Task </center >

| Tasks | Files | Description |
| ----- | ----- | ------ |
|Task 0: Fork me if you can!| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/AUTHORS | Fork another github repository to work on it as the code base |
|Task 1: Bug free| https://github.com/AndrewKalil/AirBnB_clone_v2/tree/master/tests/ | Test cases for the project |
|Task 2: Console improvement| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/console.py | Improve the consoe in odrder to receive a number of arguements that can be saved in database |
|Task 3: MySQL setup development| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql | To create the MySQL databse |
|Task 4|  |  |
|Task 5|  |  |
|Task 6|  |  |
|Task 7|  |  |
|Task 8|  |  |
|Task 9|  |  |
|Task 10|  |  |
<br >
<br >
<center > <h2 > General Use </center >

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

# Commands
+ Crete a new object.
+ Retrieve an object from a file, database, etc.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update object's attributes.
+ Destroy an object.

#### Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. followed by its parameters. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>


# Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

    Usage: < class_name > . < command > ([ < id > [name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands:

    * all - Shows all objects the program has access to, or all objects of a given class

        * count - Return number of object instances by class

    * show - Shows an object based on class and UUID

        * destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br >
<br >
<center > <h1> Examples </center >
<h3 > Primary Command Syntax

# Example 0: Create an object
Usage: create < class_name >
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
```
# Example 1: Show an object
Usage: show < class_name > <_id >

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel](3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
                                                   'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
```
# Example 2: Destroy an object
Usage: destroy < class_name > <_id >
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)
```
# Example 3: Update an object
Usage: update < class_name > <_id >
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel](b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
                                                   'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3 > Alternative Syntax

# Example 0: Show all User objects
Usage: < class_name > .all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}",
 "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

# Example 1: Destroy a User
Usage: < class_name > .destroy( < _id > )
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb)[
    "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
# Example 2: Update User (by attribute)
Usage: < class_name > .update( < _id > , < attribute_name > , < attribute_value > )
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb)[
    "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
# Example 3: Update User (by dictionary)
Usage: < class_name > .update(< _id > , < dictionary > )
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb)["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br >
