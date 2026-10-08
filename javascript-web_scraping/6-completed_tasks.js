#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = {};
    for (const todo of JSON.parse(body)) {
      if (todo.completed) {
        tasks[todo.userId] = (tasks[todo.userId] || 0) + 1;
      }
    }
    console.log(tasks);
  }
});
