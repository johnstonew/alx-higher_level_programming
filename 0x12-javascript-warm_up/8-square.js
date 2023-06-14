#!/usr/bin/node
const sizeArgument = process.argv[2];
const size = parseInt(sizeArgument);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
