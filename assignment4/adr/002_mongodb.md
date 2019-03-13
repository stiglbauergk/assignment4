# Choice of Database Management System

# Status: accepted

# Context:

An example of a Dockerized Web app is needed that supports all CRUD functions:
1. Create - the app needs to be able to take user input and add that input into
the correct table in the correct format.
2. Read - the app needs to be able to read and display contents of the
connected database.
3. Update - the app needs to be able to edit contents of the database using the
interface and make those changes to content in the actual database as well.
4. Delete - the app needs to be able to provide a way to delete contents from
the database using the interface.

The application should also be RESTful, meaning it, according to IBM's developerWorks,
follows four principles:
1. Uses HTTP methods
2. Is stateless
3. Expose directory structure-like URI's.
4. Transfer XML, JSON, or both.

# Decision:

MongoDB is an easy-to-use database management system that I am familiar with and that
incorporates well with Node.js. MongoDB Docker containers are readily available
 in the Docker Hub. MongoDB supports BASE transactions which will allow for scalability,
 and any problems with Consistency from a lack of ACID transactions can be minimized
 by the "Eventual consistency" of BASE transactions.


# Consequences:

Minimal effort is required to make the environment operational. The version of
MongoDB used in the app (3.5.2) does not support ACID transactions. The only big
issue from a lack of ACID transactions would come from Consistency and duplicate
data, but this issue could be offset by the use of Keys in the database collections.
