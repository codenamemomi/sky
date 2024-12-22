This is  RAW api server side with the use of RESTFULAPI framework helps to handle a library like web application, this web appliction consit of two branches, the branch that
does a CRUD operation and deals with the BOOKS and the branch that also does a CRUD operation that deals with the AUTHOR. WHAT IS REST?
REST API stands for Representational State Transfer Application Programming Interface. It's a set of guidelines for designing APIs that communicate between two systems, 
a client and a server, over a network. REST APIs are a common way to connect applications and components in microservices architectures. And with the use of the API
we are able to impliment the CRUD function into this web server side application. WHAT IS CRUD?
CRUD is an acronym for the four basic functions of a computer database: create, read, update, and delete. These functions are used to perform operations on data in 
relational databases and the applications that manage them. HOW DOES IT WORK?
In the code i have created models and formats that deals with the handlinng of input and information and with the use of serializer it turns a python dictionary into a JSON
and stores the information with the use of SQLite.
You can access the web app directly from the webpage by following the simple webpage urlpath or also using teh same url path access the information with api access apps like
POSTMAN

THIS ARE THE URL MAPPING TO EACH APP AND ITS MODELS:
AppOne : This app is the one that deals with BOOKS, to access this apps information use 
        http://(server site)/appone/books/
    using this in either the postman app or the webpage gives direct access to view the framework
    and if you want to access or view a particular book you could still use this : http://(server site)/appone/books/(the index or id of the book)

AppTwo  : This app specially deals the information on the author and ive connecte that if you have a book in your database and the author inputed wrote it you can add it
    to th authors details, to access this apps information use
        http://(server site)/apptwo/authors/
    using this in either the postman app or the webpage gives direct access to view the framework
    and if you want to access or view mor edetail about an author you could still use this : http://(server site)/apptwo/authors/(the index or id of the author)
