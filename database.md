Install postgres :-
        ```
        $ sudo apt-get update
        $ sudo apt-get install postgresql postgresql-contrib
        ```
        
        
        ```
        For Mac Users:-
        Goto :- http://postgresapp.com/
        and read Quick Installation Guide(Just three steps)
        ```

Activate Virtualenv.


Install supported pacakages :-
        ```
        $ pip install -r requirements.txt
        ```

Do Following stps :-

Note:- if you are getting some error like 'directory doesn't exists' then do the Following and try step 1 again.
        ```$sudo service postgresql restart```
```
    1.    $ sudo su - postgres
```
```
    2.    $ psql -d template1 -U postgres
              template1=# CREATE USER newseusername WITH PASSWORD 'newpassword';
              template1=# CREATE DATABASE databasename;
              template1=# GRANT ALL PRIVILEGES ON DATABASE databasename to newseusername;
              template1=# \q
```        
        
Ignore if you get any History File(Permission denied) warning on "\q" command.

    3. Edit newseusername, newpassword and databasename in database_info.py file.

    4. $python manage.py initdb
        

if you got only warnings and not any errors like 'database doesn't exists' etc. then the database is created.
