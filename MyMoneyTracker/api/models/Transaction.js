/*
    A simple "import {mode, Schema} from 'mongoose'" would not work in Node.js. Instead, we use the require()
    function to load and cache the mongoose module. The below lines of code are used to import the mongoose
    module and the Schema class from the mongoose module.

    By using the import statement an error occurs because Node.js is trying to use the import statement in a
    context that doesn't recognize it as part of an ECMAScript module. By default, Node.js treats files as
    CommonJS modules.
*/

const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const model = mongoose.model;

/*
    The variable TransactionSchema is assigned a new instance of the Schema class from the mongoose module.
    The Schema class is a constructor function that creates a new schema object. A schema is a blueprint for a
    MongoDB collection that defines the structure of the documents within that collection. In this case, the
    TransactionSchema schema defines the structure of documents in the transactions collection. The schema defines
    the fields that documents in the collection will have, as well as the data types and any constraints on the data.
    The schema is used to validate documents before they are inserted into the database. The schema is a JSON object
    that contains key-value pairs, where the key is the name of the field and the value is an object that specifies
    the data type and any constraints on the field.
*/
const TransactionSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    description: {
        type: String,
        required: false
    },
    date: {
        type: Date,
        required: true
    }
});

/*
    The variable TransactionModel is assigned the return value of the model() function from the mongoose module.
    The function is used to create a new model object. A model is a class that represents a collection in the
    database and is used to create, read, update, and delete documents in the collection. The model() function
    takes two arguments: the name of the model and the schema that defines the structure of the documents in the
    collection. In this case, the model is named "Transaction" and the schema is the TransactionSchema schema
    defined above. The TransactionModel model represents the transactions collection in the database and is used
    to interact with the collection.
*/
const TransactionModel = model('Transaction', TransactionSchema);

/*
    This serves to export the TransactionModel from the current module so that it can be imported and used in
    other modules or files within the application. With this the TransactionModel becomes accessible to other
    parts of the application that require() this module
    module - a reference to the current module, and in Node.js, every file is treated as a separate module
    exports - an object that the current module can add properties to in order to export them, and anything
    attached to it will be exposed as the module's public API
    TransactionModel - the object being exported, which is the model representing the transactions collection

    ** See index.js: 28 for an example of how this module is imported and used in another file **
*/
module.exports = TransactionModel;
