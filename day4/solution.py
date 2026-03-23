import copy;
from util import read_dataset;

# if @ < 3 pick

def countValue(val, table, coordinates) -> int:
  counter: int = 0;

  for x,y in coordinates:
    oob: bool = x < 0 or y < 0 or x > len(table) -1 or y > len(table[0]) -1;

    if oob == True:
      continue;
    if table[x][y] == '@':
      counter += 1;
  
  return counter;

def countAdjacent(coordinates: tuple[int, int], table: list[str]) -> int:
  x, y = coordinates;
  check: list[tuple[int, int]];
  
  check = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)];

  return countValue('@', table, check);

def extractRolls(table: list[str]) -> tuple[int, str]:
  accessible: int = 0;
  newTable: list[str] = copy.deepcopy(table);

  for r, row in enumerate(table):
    for c, col in enumerate(row):
      coordinates: tuple[int, int] = (r, c);

      if table[r][c] == '.':
        newTable[r][c] = '.';
        continue;
      else:
        newTable[r][c] = '@';

      surroundingItems:int = countAdjacent(coordinates, table);
      # print(f"{r,c}: {surroundingItems}");

      if surroundingItems < 4:
        accessible += 1;
        newTable[r][c] = 'x';

  return [accessible, newTable];
    
dataset = read_dataset(__file__);
rows = dataset.split("\n");
table: list[str] = [];

for row in rows:
  table.append(list(row));

rollsExtracted, newTable = extractRolls(table);
lastExtraction = rollsExtracted;
keepExtracting = True;

while keepExtracting:
  rollsExtracted, newTable = extractRolls(newTable);
  # print(newTable);
  keepExtracting = False if rollsExtracted - lastExtraction == 0 else True;
  lastExtraction = rollsExtracted;

print(rollsExtracted);
  