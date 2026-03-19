import sys;

inputFile: str = sys.argv.pop(1);

with open(inputFile) as f:
  dataset = f.read();

entries: list[str] = dataset.split(',');
duplicates: list[int] = [];

for entry in entries:
  ranges: [str, str] = entry.split('-');
  start: int = int(ranges[0]);
  end: int = int(ranges[1])+1;
  
  for n in range(start, end):
    nStr = str(n);
    nLen = len(nStr);
    
    if nLen%2 != 0:
      continue;

    sliceAtIndex: int = len(nStr) // 2

    if nStr[:sliceAtIndex] == nStr[sliceAtIndex:]:
      duplicates.append(n);

# print(sum(duplicates));

for entry in entries:
    ranges: [str, str] = entry.split('-');
    s: int = int(ranges[0]);
    e: int = int(ranges[1])+1;

    for n in range(s, e):
      m: int = 0;
      nStr = str(n);
      nLen = len(nStr);
      i: int = 1;
      p: str = nStr[0];

      if nLen<3:
        continue;
      
      while i < nLen:
        pLen = len(p);


        c = nStr[i:i+pLen];
        # print(f"p: {p} | match: {p} v {c} | pLen: {pLen} | t: {i}:{i+pLen} | i: {i} |  nStr: {nStr} | m: {m}");

        if (p == c):
          m += 1;
          p = c;
          i += pLen;
        else:
          p = nStr[0:i+1];
          m = 0;
          i = len(p);

      if m>=2:
        if n not in duplicates:
          duplicates.append(n);

dupeSum:int = sum(duplicates);
expected:int = 4174379265
# assert dupeSum == expected, f"Expected: {expected} | Actual {dupeSum} | Duplicates: {duplicates}";

print(f"Sum: {sum(duplicates)}");