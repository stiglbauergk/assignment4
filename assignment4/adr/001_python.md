# Choice of Content Management System

# Status: changed, accepted

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

Python is an easy-to-implement easy-to-use environment that incorporated well with
MongoDB. Docker containers are readily available in the Docker Hub.

The use of Python allowed implementing CRUD operations easy,
using GET, POST, and DELETE HTTP methods.

The use of Python and HTTP methods was the first step towards creating a RESTful API. A RESTful
app is important for this app because I do not know what kind of platform or
interface a hypothetical user would be using. HTTP services are on almost allow machines and OS's so this gives my app universality.


# Consequences:
A change was made from Node.js to Python after difficulties arose implementing
Node.js app.

Minimal effort is required to make the environment operational.
