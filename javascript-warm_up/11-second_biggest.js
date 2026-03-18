#!/usr/bin/node
(function () {
  const args = process.argv.slice(2);
  const numbers = args.map(Number);
  let numberone = -Infinity;
  let numbertwo = -Infinity;
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > numberone) {
      numbertwo = numberone;
      numberone = numbers[i];
    } else if (numbers[i] > numbertwo) {
      numbertwo = numbers[i];
    }
  }
  if (numbers.length === 0 || numbers.length === 1) {
    console.log(0);
  } else {
    console.log(numbertwo);
  }
})();
