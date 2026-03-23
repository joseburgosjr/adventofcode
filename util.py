from pathlib import Path


def read_dataset(caller_file: str) -> str:
    return (Path(caller_file).parent / "dataset.txt").read_text()
