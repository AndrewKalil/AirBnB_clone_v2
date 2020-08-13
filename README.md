<center > <h1 > HBNB clone - MySQL </center > :computer:

In this project we will do two things as part of the main and bigger project: HBNB Clone. We will replace the file storage by a Database storage and map your models to a table in database by using an O.R.M.
---

<center > <h3 > Repository Contents by Project Task </center >

| Tasks | Files | Description |
| ----- | ----- | ------ |
|Task 0: Fork me if you can!| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/AUTHORS | Fork another github repository to work on it as the code base |
|Task 1: Bug free| https://github.com/AndrewKalil/AirBnB_clone_v2/tree/master/tests/ | Test cases for the project |
|Task 2: Console improvement| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/console.py | Improve the consoe in odrder to receive a number of arguements that can be saved in database |
|Task 3: MySQL setup development| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql | To create the MySQL databse |
|Task 4: MySQL setup test| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/setup_mysql_test.sql | To create a test MySQL server |
|Task 5: Delete Object| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/models/engine/file_storage.py | Delete objects from the databse |
|Task 6: DBStorage - States and Cities| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/models/ | Link python codebase to database using SQLalchemy to complete the models for states and cities |
|Task 7: DBStorage - User| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/models/ | Link python codebase to database using SQLalchemy to complete the models for users |
|Task 8: DBStorage - Place| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/models/ | Link python codebase to database using SQLalchemy to complete the models for place |
|Task 9: DBStorage - Review| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/models/ | Link python codebase to database using SQLalchemy to complete the models for review |
|Task 10: DBStorage - Amenity... and BOOM!| https://github.com/AndrewKalil/AirBnB_clone_v2/blob/master/models/ | Link python codebase to database using SQLalchemy to complete the models for amenity |
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

## Tests

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

```python3 -m unittest discover tests ```

from the root directory.

## Set-up

### Database Set-up
Project will be using MySQL server for its data storage which will use (at this time) a database `hbnb_dev_db` as the user `hbnb_dev`. The user's default credentials are `hbnb_dev_pwd`.

In order to perform this configuration, you can run the following commands:

```cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p```

by providing your root password.

```echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db```

will show you that you successfully created your database.

```echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p```

will show you the specific privileges the user has on the different databases.

## Bugs

+ No known bugs at this time.