# Configuration Data
The configuration data necessary for this application includes the database shell files and the Docker files. The database shell files initially create the KillCounter database and populates the database with a few initial gamers. This database is then used to store the edits and adds that may come from the Web app.

The Docker files were used to make data persistence efficient. The docker-compose file incorporates volumes in order to persist the data.

Since this data is not very
sensitive or proprietary, it is not necessary to set restraints on who
may edit or access the data.

There is not much need for failure backup/disaster protection for such a simple app.

# Operational Data
The transactional data comes from the Python app. The Python app had to incorporate transactional data in order to update the database using the app.

For this app, restraints were not important, and it was not really possible to edit the schema or structure of the data or database.
