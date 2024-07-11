/* 
    Imports the Express library, a fast, unopinionated, minimalist web framework for Node.js It is used to create 
    web applications and APIs. The require() function is used to load and cache JavaScript modules. The express variable
    is assigned the express module
*/
const express = require('express');

/*
    Imports the cors library, which is a Node.js package used to enable Cross-Origin Resource Sharing (CORS) in 
    Express applications. CORS is a mechanism that allows resources on a web page to be requested from another
    domain outside the domain from which the resource originated. The require() function is used to load and cache
    JavaScript modules. The cors variable is assigned the cors module.
*/
const cors = require('cors');

/*
    Loads environment variables from a .env file into process.env. The require() function is used to load and cache
    JavaScript modules. The dotenv variable is assigned the dotenv module. The dotenv.config() function is called
    to load the environment variables from the .env file into process.env
*/
require('dotenv').config();

/*
    Imports the TransactionModel model from the Transaction module. The require() function is used to load and cache
    JavaScript modules. The TransactionModel variable is assigned the TransactionModel model from the Transaction
    module.
*/
const TransactionModel = require('./models/Transaction.js');

/*
    Imports the mongoose library, which is a MongoDB object modeling tool designed to work in an asynchronous
    environment. Mongoose provides a straight-forward, schema-based solution to model application data. The require()
    function is used to load and cache JavaScript modules. The mongoose variable is assigned the mongoose module.
*/
const mongoose = require('mongoose');

/*
    The express() function is a top-level function exported by the express module. The express() function is a 
    creates an Express application. The app variable is assigned the return value of the express() function
*/
const app = express();

/* 
    Mounts the cors() middleware function at the root path, applying it to all routes. This enables 
    Cross-Origin Resource Sharing (CORS) in the Express application, allowing resources on a web page to be
    requested from another domain outside the domain from which the resource originated.
*/
app.use(cors());

/*
    A middleware that that tells the Express app to automatically parse incoming requests with JSON payloads.
    This means that it converts the JSON payload of incoming requests into JavaScript objects before reaching the
    request handlers. The use() function is used to mount the middleware function on the Express application stack while
    the express.json() function is a built-in middleware function in Express that parses incoming requests with
    JSON payloads. Essentially, it looks at the "Content-Type" header of incoming requests and if the content type is
    "application/json", it parses the body of the request into a JavaScript object. After parsing, this object is
    available on req.body.
*/
app.use(express.json());

/*
    Defines a route handler for the GET request to the path /api/test. When a GET request is made to this path,
    the call back is executed. In this case, the callback function takes two parameters, request and response.
    The request object represent the HTTP request and has properties for the request query string, parameters, body,
    HTTP headers, and more. The response object represent the HTTP response that an Express app sends when it receives
    an HTTP request. In this case, it sends back a JSON response containing the string "Test Passed!"
*/
app.get('/api/test', (request, response) => {
  response.json("Test Passed!");
});

/*
    Defines a route handler for the POST request to the path /api/transaction. When a POST request is made to this path,
    the call back is executed. In this case, the callback function takes two parameters, request and response.
    The request object represent the HTTP request and has properties for the request query string, parameters, body,
    HTTP headers, and more. The response object represent the HTTP response that an Express app sends when it receives
    an HTTP request. In this case, it sends back a JSON response containing the body of the request.

    The await keyword is used to tell JavaScript to wait for the completion of the asynchronous operation before
    continuing. In this case, it tells JavaScript to wait for the connection to the MongoDB database to be established
    before continuing.
    
    The mongoose.connect() function is used to connect to the MongoDB database. It takes a URL string as an argument
    that specifies the location of the database. The URL string is stored in the MONGO_URL environment variable, which
    is loaded from the .env file. The connection to the database is established using the await keyword, which tells
    JavaScript to wait for the connection to be established before continuing.

    The request.body object contains the data sent in the request body. In this case, it contains the name,
    description, and date of the transaction. The data is extracted from the request body using object destructuring
    and stored in variables.
*/
app.post('/api/transaction', async (request, response) => {
    await mongoose.connect(process.env.MONGO_URL);
    const {name, price, description, date} = request.body;
    const newTransaction = await TransactionModel.create({name, price, description, date});
    response.json(newTransaction);
});

app.get('/api/transactions', async (request, response) => {
    await mongoose.connect(process.env.MONGO_URL);
    const transactions = await TransactionModel.find();
    response.json(transactions);
});

/*
    Tells the Express application to listen for incoming connection on port 4040. This effectively starts the server,
    and it will remain running as long as the application is running. The server will listen on port 4040, and any
    incoming requests will be handled by the Express application
*/
app.listen(4040);
