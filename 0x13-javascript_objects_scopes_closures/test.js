#!/usr/bin/node
const personPrototype = {
    greet() {
      console.log(`hello, my name is ${this.name}!`);
    },
  };
  
  function Person(name) {
    this.name = name;
  }
  const person = new Person('mohamed');
  Object.assign(Person.prototype, personPrototype);
  let object = person;

  do {
    object = Object.getPrototypeOf(object);
    console.log(object);
  } while (object);
