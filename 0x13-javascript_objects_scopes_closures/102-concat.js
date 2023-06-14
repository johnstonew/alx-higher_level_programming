#!/usr/bin/node
const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

const content1 = fs.readFileSync(sourceFile1, 'utf8');
const content2 = fs.readFileSync(sourceFile2, 'utf8');
const concatenatedContent = content1 + content2;

fs.writeFileSync(destinationFile, concatenatedContent);

console.log('Files concatenated successfully!');
