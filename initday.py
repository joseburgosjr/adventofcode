import sys;
import http.client;
from pathlib import Path;

arg: str = sys.argv.pop(1);
year, day = arg.split("/");
tokenFile = Path('session.token');

with tokenFile.open() as f:
  token = f.readline();

folder = f"./day{day}";
# create day folder from argv
p = Path(folder);
p.mkdir();
# create dataset.txt from data retrieved from https://adventofcode.com/y/day/d/input
(p / "dataset.txt").touch();
(p / "solution.py").write_text("from util import read_dataset;\n\ndataset = read_dataset(__file__);\n");
(p / "revision.py").touch();

conn = http.client.HTTPSConnection("adventofcode.com");
conn.request("GET", f"/{year}/day/{day}/input", headers={ "Cookie": f"session={token}" });
response = conn.getresponse();

if response.status == 200:
  (p / "dataset.txt").write_text(response.read().decode("utf-8"));
else:
  print(f"Failed: {response.status} {response.reason}");
