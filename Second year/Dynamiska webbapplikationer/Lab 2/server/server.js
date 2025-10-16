const express = require('express');
const server = express();
const sqlite3 = require('sqlite3').verbose();

server
  .use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    next();
  })
  .use(express.json())
  .use(express.urlencoded({ extended: false }));

server.get('/users', (req, res) => {
  const db = new sqlite3.Database('./gik339-labb2.db');
  const sql = 'SELECT * FROM USERS';
  db.all(sql, (err, rows) => {
    if (err) {
      res.status(500).send(err);
    } else {
      res.send(rows);
    }
  });

  db.close();
});

server.post('/users', (req, res) => {
  const { firstName, lastName, username, color } = req.query;
  const db = new sqlite3.Database('./gik339-labb2.db');
  const sql = 'INSERT INTO USERS (firstName, lastName, username, color) VALUES (?, ?, ?, ?)';
  const params = [firstName, lastName, username, color];
  db.run(sql, params, (err) => {
    if (err) {
      res.status(500).send(err);
    } else {
      res.send({ id: this.lastID, firstName, lastName, username, color });
    }
  });
  db.close();
});

server.delete("/users/:id", (req, res) => {
  const id = req.params.id;

  const db = new sqlite3.Database('./gik339-labb2.db');
  const sql = 'DELETE FROM USERS WHERE id=?';

  db.run(sql, id, (err) => {
    if (err) {
      res.status(400).send(err);
    } else {
      res.send({ "message": `User with ID ${id} deleted.` })
    }
  });

  db.close();
});

server.listen(3000, () => {
  console.log("Server started on port 3000");
});