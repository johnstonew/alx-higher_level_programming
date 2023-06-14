#!/usr/bin/node
const firstArgument = process.argv[2];
const numOccurrences = parseInt(firstArgument);

if (isNaN(numOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
