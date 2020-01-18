#!/usr/bin/env python3

import sys

def fibonacci(n, l):
    # Casting to int to showcase the unit test functionality
    start = int(n)
    length = int(l)

    if length == 0:
        print('Length should be more than 0')
        return

    results = getSequence(start, length)
    print(results)
    writeToFile(results)

def getSequence(start, length):
    results = []

    # if starting number is 0 we need to append extra 1
    if start == 0:
        results.append(1)

    value = 1
    prevValue = 0

    while len(results) < length:
        tmp = prevValue + value
        prevValue = value
        value = tmp

        if value > start:
            results.append(value)

    return results


def writeToFile(seq):
    with open('fib_sequence.txt', "w") as file:
        for i in seq:
            file.write(str(i) + '\n')

        file.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Not enough arguments, usage: fibonacci.py <start> [<count>]')
    else:
        # Get start and length values, length defaults to 10
        fibonacci(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 10)
