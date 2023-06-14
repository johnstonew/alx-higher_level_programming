#!/usr/bin/node
exports.converter = function(base) {
  if (base <= 1) {
    return;
  }

  exports.converter = function(number) {
    if (number >= base) {
      exports.converter(Math.floor(number / base));
    }
    process.stdout.write((number % base).toString());
  };
};
