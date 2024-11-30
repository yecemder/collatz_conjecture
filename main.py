from time import perf_counter_ns as time
from pathlib import Path
import os
import sys

MAX_START_VAL = 1_000_000

def next_collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    

def collatz(max_val):
    skipped = 0
    collatz_nextval = [0] * (max_val + 1)
    for start_val in range(1, max_val + 1):
        # Every 5%, print progress
        # if start_val % (max_val // 20) == 0:
        #     print(f"Progress: {start_val:,}/{max_val:,} ({start_val / max_val * 100:.2f}%)")
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
    print(f"Skipped {skipped} values out of {max_val} ({skipped / max_val * 100:.2f}%)")
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
    print("Collatz took", (end - start) / 1e9, "seconds")
    
    output = output[1:]
    output_dir = Path(__file__).parent / "outputs" # Directory for outputs
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = output_dir / f"collatz-{MAX_START_VAL:_}.txt"
    
    print("Formatting output...")
    formatStart = time()
    formatted = format_output(output)
    formatEnd = time()
    print("Output formatting took", (formatEnd - formatStart) / 1e9, "seconds")
    
    
    print("Writing output to", output_path)
    writeStart = time()
    with open(output_path, "w") as f:
        f.write(formatted)
    writeEnd = time()
    print("Output written in", (writeEnd - writeStart) / 1e9, "seconds")


if __name__ == "__main__":
    main()
    
# 4
# 35
# 349
# 3492
# 34895
# 3489368
# 34893828
