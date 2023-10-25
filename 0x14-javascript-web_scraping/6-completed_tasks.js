#!/usr/bin/node
// completed tasks
const request = require('request');
const options = {
  method: 'GET',
  uri: `${process.argv[2]}`
};
request(options, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};
    let userId = 1;
    let counter = 0;
    for (let i = 0; userId < tasks.length && i < tasks.length; i++) {
      const currentUserId = userId;
      const task = tasks[i];
      userId = task.userId;
      if (userId !== currentUserId) {
        completedTasks[currentUserId] = counter;
        counter = 0;
      }
      if (task.completed) {
        counter++;
      }
    }
    if (counter !== 0) {
      completedTasks[userId] = counter;
    }
    console.log(completedTasks);
  }
});
