import {useEffect, useState} from 'react';
import React from 'react';
import './App.css';

function App() {
  // useState is a hook that allows you to add state to a functional component
  // Creates a variable named "name" and a function called setName to update it w/ the initial value of "name" being ''
  // Whenever setName is called with a new value, the "name" state variable will be updated w/ that new value and the component will re-render
  const [name, setName] = useState('');

  // The above description/comments apply for the below three lines as well
  const [price, setPrice] = useState('');
  const [date, setDate] = useState('');
  const [description, setDescription] = useState('');
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    getTransactions().then(setTransactions);
  }, []);
 
  async function getTransactions() {
    const url = process.env.REACT_APP_API_URL + '/transactions';
    const response = await fetch(url);
    return await response.json();
  }

  function addNewTransaction(event) {
    // Prevents the default behavior of the form when it is submitted
    event.preventDefault();

    // The URL of the API is stored in the REACT_APP_API_URL environment variable in the .env file
    const url = process.env.REACT_APP_API_URL + '/transaction'
    
    /*
      Initiates a fetch request to the specified url. The second argument is an options object that configures the
      specifics of the request:
        method: 'POST' - specifies that this is a POST request, indicating that data should be sent to the server
        headers: {'Content-type': 'application/json'} - tells the server the format of the data being sent is JSON
        body: JSON.stringify({name, description, date}) - converts the data (name, description, date) to a JSON
        string before sending it to the server

      The response variable below utilized as a parameter for the .then() method is the response object returned
      by the fetch request. The response object contains information about the response to the request, such as the
      status code, headers, and body of the response. It provides methods to handle the response data and properties
      to inspect the response. In the below code, the response.json() method is used to parse the JSON body response.

      .then(response => {...}) - a Promise that resolves with the response to the request. The response object is passed
      to the first .then() method, which returns another Promise that resolves with the result of parsing the response body
      as JSON

      response.json() - called on the response object, reading the response stream to completion and parses the
      response body as JSON and returns a Promise that resolves with the result of parsing the body text as JSON

      .then(json => {...}) - a Promise that resolves with the result of parsing the response body as JSON
      The parsed JSON object is passed to the callback function, which logs the result to the console
    */
      fetch(url, {
        method: 'POST',
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify({
          name,
          price,
          description,
          date
        })
      }).then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      }).then(json => {
        setName('');
        setPrice('');
        setDate('');
        setDescription('');
        console.log('result', json);
      }).catch(error => {
        console.error("Failed to fetch or parse response:", error);
      });
  }

  // The balance is calculated by summing the price of all transactions
  let balance = 0;
  for (const transaction of transactions) {
    balance += transaction.price;
  }

  // The balance is formatted to two decimal places
  balance = balance.toFixed(2);

  // The cents part of the balance is extracted
  const cents = balance.split('.')[1];

  // The dollar part of the balance is extracted
  balance = balance.split('.')[0];

  return (
    <main> 
      {/* This is the main content of the page. The main tag is a parent element and contains several children elements */}
      {/* The span tag is a child element of the h1 tag. Its purpose is to style the decimal part of the price */}
      <h1>${balance}<span>.{cents}</span></h1>
      <form onSubmit={addNewTransaction}>
        <div className="basic-info">
          <input type="text"
                 // Sets the value to the current value of the "name" state variable
                 value={name} 
                 // Whenever the input field changes, the setName function is called with the new value
                 // event is the event object that is passed to the function
                 // event.target is the input field that triggered the event
                 // event.target.value is the new value of the input field
                 // when an event occurs the setName function is called which updates the value of "name" w/ the new value from the input fieldx
                 onChange={event => setName(event.target.value)}
                 placeholder="Transaction Name"/>
          <input type="text" 
                 value={price}
                 onChange={event => setPrice(event.target.value)}
                 placeholder="+/- Amount"/>
        </div>

        <div className="description-and-date">
          <input value={date}
                 onChange={event => setDate(event.target.value)}
                 type="datetime-local"/>
          <input value={description} 
                 onChange={event => setDescription(event.target.value)}
                 type="text"
                 placeholder="Description"/>
        </div>

        {/* The button tag is a child element of the form tag. It is used to submit the form */}
        <button type="submit">Add Transaction</button>
      </form>

      <div className="transactions">
        {/* The left side contains the name and description of the transaction */}
        {/* The right side contains the price and date of the transaction */}

        {transactions.length > 0 && transactions.map(transaction => {
          return (
            <div className="transaction">
              <div className="left">
                <div className="name">{transaction.name}</div>
                <div className="description">{transaction.description}</div>
              </div>
              <div className="right">
                <div className={"price " + (transaction.price >= 0 ? 'green' : 'red')}>
                  -${transaction.price}
                </div>
                <div className="date">2024-06-24</div>
              </div>
            </div>
          );
        })}
      </div>
    </main>
  );
}

export default App;
