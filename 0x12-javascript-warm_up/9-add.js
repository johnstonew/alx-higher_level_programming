#!/usr/local/bin/node
function add (a, b) {
  return a + b;
}

const firstArgument = process.argv[2];
const secondArgument = process.argv[3];

const num1 = parseInt(firstArgument);
const num2 = parseInt(secondArgument);

result = add(num1, num2);
console.log(result);
