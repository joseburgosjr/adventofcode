import sys;

inputFile: str = sys.argv.pop(1);

with open(inputFile) as f:
  dataset = f.read();

def findHighest(text: str, currentPosition: int, limit: int) -> tuple[int, int]:
  textLen = len(text);
  remaining: str = text[currentPosition:textLen-limit];
  # print(f"{currentPosition}:{textLen-limit}");
  # print(remaining);
  highestValue: int = 0;
  highestIndex: int = 0;

  for i, char in enumerate(remaining):
    if char == '9':
      highestValue = 9;
      highestIndex = i;
      break;

    num: int = int(char);

    if num > highestValue:
      highestValue = num;
      highestIndex = i;

  return [highestIndex+currentPosition, highestValue];

entries: list[str] = dataset.split("\n");
jolts: list[int] = [];
maxBatteries: int = 12;

for entry in entries:
  maxJoltsForBank: list[str] = [];
  currentBatteriesLeft: int = maxBatteries;
  index: int = 0;

  while currentBatteriesLeft != 0:
    currentBatteriesLeft -= 1;
    index, value = findHighest(entry, index, currentBatteriesLeft);
    maxJoltsForBank.append(str(value));
    index += 1;

  jolts.append(int("".join(maxJoltsForBank)));

print(sum(jolts));
