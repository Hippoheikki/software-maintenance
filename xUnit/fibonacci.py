#!/usr/bin/env python3

import sys

def fibonacci(arguments):
    if len(arguments) == 0:
        raise RuntimeError("Not enough arguments, usage: fibonacci <start> [<length>]")


    # Casting to int to showcase the unit test functionality
    start = int(arguments[0])
    length = int(arguments[1]) if len(arguments) > 1 else 10

    if length == 0:
        raise RuntimeError("Length should be more than 0")
        return

    results = getSequence(start, length)
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
        string = ",".join(str(i) for i in seq)
        file.write(string)
        file.close()

if __name__ == "__main__":
    # Remove first argument which is the filename
    fibonacci(sys.argv[1:])
