import time
import os
import sys

MAX_START_VAL = 1000000

def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    

def collatz(max_val):
    COLLATZ_SEQUENCE = [None] * (max_val + 1)
    for start_val in range(1, max_val + 1):
        pass