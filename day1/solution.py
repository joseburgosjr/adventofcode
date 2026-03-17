import sys;

# Learned after finding modular arithmatic again
def combinationLoop(startingPoint: int, amount: int) -> int:
  limit: int = 100;
  moveTo: int = (startingPoint + amount) % limit;

  return moveTo;

# realized (after too much time) the looping logic needed to be separated 
# because the startingPoint was interferring with the current iterator
def loopIteration(current: int, amount: int) -> tuple[int, int]:
  totalSteps: int = abs(amount);
  looped: int = 0;

  for i in range(totalSteps):
    if amount < 0:
      current -= 1;
    else:
      current += 1;

    if (current%100) == 0:
      # print(f"current: {current} step: {i}");
      looped+=1;

  return [current, looped];

def solveCombination(items: list[int] = [], currentValue: int = 50) -> tuple[int, int]:
  solutionOne: int = 0;
  solutionTwo: int = 0;
  current: int = 50;

  for amount in items:
    currentValue = combinationLoop(currentValue, amount);
    current, loops = loopIteration(current, amount)
    solutionTwo += loops;

    if currentValue == 0:
      solutionOne += 1;

  return [solutionOne, solutionTwo];

def readInput(file: str) -> list[int]:
  inputs: list[int] = [];

  with open(file) as f:
    data = f.read();

  entries = data.split("\n")

  for entry in entries:
    multiplier = 1 if entry[0] == 'R' else -1;
    inputs.append(int(entry[1:]) * multiplier)

  return inputs;