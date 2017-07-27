from docutils.core import publish_string
import sys


def main():
    filename = sys.argv[1]
    with open(filename, mode='rt') as f:
        rst = f.read()
    print(publish_string(rst).decode('utf-8'))
