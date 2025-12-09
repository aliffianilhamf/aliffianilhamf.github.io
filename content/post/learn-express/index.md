---
title: Learn Express.js - A Beginner's Guide to Building Web Applications with Node.js
summary: This post introduces Express.js, a popular web framework for Node.js, and guides you through setting up a basic web application.
date: 2025-12-09
authors:
  - admin
tags:
  - Express.js
  - Node.js
  - Web Development
---

## Introduction to Express.js

Express.js is a popular web application framework for Node.js that simplifies the process of building web applications and APIs. It provides a robust set of features for web and mobile applications, making it easier to handle routing, middleware, and server-side logic.

## Setting Up Environment

Before we start building an Express.js application, ensure you have Node.js and npm (Node Package Manager) installed on your machine. You can download them from the [official Node.js website](https://nodejs.org/).
Once you have Node.js and npm installed, you can create a new directory for your Express.js project and navigate into it:

```bash
mkdir my-express-app
cd my-express-app
```

Next, initialize a new Node.js project by running:

```bash
npm init -y
```

This command will create a `package.json` file in your project directory.

## Installing Express.js

To install Express.js, run the following command in your project directory:

```bash
npm install express
```

This command will download and install Express.js and its dependencies.

## Hello World with Express.js

Now, let's create a simple "Hello World" application using Express.js. Create a new file named `app.js` in your project directory and add the following code:

```javascript
const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

This code sets up a basic Express.js server that listens on port 3000 and responds with "Hello World!" when the root URL is accessed.

To run the application, use the following command in your terminal:

```bash
node app.js
```

You should see a message indicating that the server is running. Open your web browser and navigate to `http://localhost:3000` to see the "Hello World!" message.

## Basic Routing

Express.js makes it easy to define routes for your application. You can create different routes to handle various HTTP methods (GET, POST, PUT, DELETE, etc.). Here's an example of defining multiple routes:

```javascript
app.get("/about", (req, res) => {
  res.send("About Page");
});

app.post("/submit", (req, res) => {
  res.send("Form Submitted");
});
```

In this example, we defined two additional routes: `/about` for GET requests and `/submit` for POST requests.

If you try to test the endpoints using a tool like Postman or curl, you'll see the appropriate responses based on the HTTP method used. For example, sending a POST request to `/submit` will return "Form Submitted". you can adding the body parser middleware to handle form data. if you want to handle JSON data, you can use `express.json()` middleware, like this:

```javascript
app.use(express.json());
```

if you want to handle URL-encoded data, you can use `express.urlencoded()` middleware, like this:

```javascript
app.use(express.urlencoded({ extended: true }));
```

## Middleware

Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the next middleware function in the application’s request-response cycle. You can use middleware to perform tasks such as logging, authentication, and error handling. Here's an example of a simple logging middleware:

```javascript
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});
```

This middleware logs the HTTP method and URL of each incoming request before passing control to the next middleware or route handler.

```javascript
const checker = (req, res, next) => {
  if (req.params.id === "1") {
    return res.send("ID 1 cannot be deleted");
  } else {
    next();
  }
};

app.delete("/user/:id", checker, (req, res) => {
  res.send(`User with ID ${req.params.id} deleted`);
});
```

In this example, the `checker` middleware checks if the `id` parameter is "1" before allowing the DELETE request to proceed.

## Integrating with a Database

To build more complex applications, you'll often need to integrate Express.js with a database. A popular choice is PostgreSQL. First, install PostgreSQL, you can refer to the [official PostgreSQL website](https://www.postgresql.org/download/) for installation instructions.
Next, install the `pg-promise` package to interact with PostgreSQL from your Express.js application:

```bash
npm install pg-promise
```

Here's a simple example of how to connect to a PostgreSQL database and perform basic CRUD operations:

```javascript
const pgp = require("pg-promise")();
const db = pgp("postgres://username:password@localhost:5432/mydatabase");

app.get("/users", async (req, res) => {
  try {
    const users = await db.any("SELECT * FROM users");
    res.json(users);
  } catch (error) {
    res.status(500).send(error.message);
  }
});
```

In this example, we connect to a PostgreSQL database and define a route to fetch all users from the `users` table.
