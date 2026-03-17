import sys;
import unittest;
import json;
from solution import solveCombination, readInput;

fileName: str = sys.argv.pop(1);
inputFile = f"./inputs/{fileName}.txt";
outputFile = f"./reddit_solutions/{fileName}.solution.json";

with open(outputFile) as f:
  solution = json.load(f);

class TestSolution(unittest.TestCase):
  def test_solve(self):
    items: list[int] = readInput(inputFile);
    firstPassword: int;
    secondPassword: int;
    [firstPassword, secondPassword] = solveCombination(items);

    if ("s1" in solution):
      self.assertEqual(firstPassword, solution["s1"]);

    self.assertEqual(secondPassword, solution["s2"]);

if __name__ == '__main__':
  unittest.main();