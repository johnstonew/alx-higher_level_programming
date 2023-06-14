#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};

exports.addMeMaybe = addMeMaybe;
