import os
import sys
import argparse


def test():
    print(dir(os.path))
    print(sys.path[0])


if __name__ == "__main__":
    test()