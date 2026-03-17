import { readFile } from 'node:fs/promises';

const startingPoint = 50;
let current = startingPoint;
let modularPoint = startingPoint;
const contents = await readFile(process.argv[2], { encoding: 'utf8' });
const limit = 100;
const steps = contents.split("\n").map((step) => {
  const amount = parseInt(step.substring(1), 10);

  return step[0] === 'L' ? -amount : amount;
});
let looped = 0;
let landOnZero = 0;

for (let i=0;i<steps.length;i++) {
  const move = Math.abs(steps[i]);
  modularPoint = (modularPoint+steps[i]) % limit;

  if (modularPoint === 0) {
    landOnZero++;
  }

  for (let j=0;j<move;j++) {
    if (steps[i] < 0) {
      current -= 1;
    } else {
      current += 1;
    }

    if (current % limit === 0) {
      looped++;
    }
  }
}
console.log({landOnZero, looped});


