#!/usr/bin/node
const argumentsList = process.argv.slice(2).map(arg => parseInt(arg));

if (argumentsList.length === 0 || argumentsList.length === 1) {
  console.log(0);
} else {
  const sortedList = argumentsList.sort((a, b) => b - a);
  console.log(sortedList[1]);
}
