#!/usr/bin/node
(function () {
  const argv = process.argv;
  if (argv.length === 2) {
    console.log('No argument');
  } else {
    console.log(argv[2]);
  }
})();
