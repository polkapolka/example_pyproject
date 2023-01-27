import argparse
import sys

from typing import List, Any


def cli():
	return main(sys.argv[1:])

def main(words: List[Any]):
	print(" ".join(map(str, words)))

if __name__ == "__main__":
	cli()