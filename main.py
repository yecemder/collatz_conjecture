from time import perf_counter_ns as time
from pathlib import Path
import os
import sys

MAX_START_VAL = 100_000_000
skipped = 0

def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    

def collatz(max_val):
    global skipped
    collatz_nextval = [0] * (max_val + 1)
    for start_val in range(1, max_val + 1):
        if collatz_nextval[start_val] != 0:
            skipped += 1
            continue
        current_val = start_val
        while (collatz_nextval[current_val] == 0):
            next_val = next_collatz(current_val)
            collatz_nextval[current_val] = next_val
            if next_val > max_val:
                break
            current_val = next_val
    
    return collatz_nextval

def format_output(output):
    # Make the output array a pretty string
    output_str = []
    for i in range(len(output)):
        output_str.append(f"{i+1}: {output[i]}")
    return "\n".join(output_str)

def main():
    start = time()
    output = collatz(MAX_START_VAL)
    end = time()
    print(f"Skipped {skipped:_} values out of {MAX_START_VAL:_}")
    print(f"Took {((end - start) / 1e3):_} microseconds to compute")
    
    # output = output[1:]
    # output_dir = Path(__file__).parent / "outputs" # Directory for outputs
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)
    # output_path = output_dir / f"collatz-{MAX_START_VAL:_}.txt"
    
    # print("Formatting output...")
    # formatStart = time()
    # formatted = format_output(output)
    # formatEnd = time()
    # print("Output formatting took", (formatEnd - formatStart) / 1e9, "seconds")
    
    # print("Writing output to", output_path)
    # writeStart = time()
    # with open(output_path, "w") as f:
    #     f.write(formatted)
    # writeEnd = time()
    # print("Output written in", (writeEnd - writeStart) / 1e9, "seconds")


if __name__ == "__main__":
    main()
    
# 4
# 35
# 349
# 3492
# 34895
# 3489368
# 34893828
