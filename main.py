from time import perf_counter_ns as time
from pathlib import Path
import os
import sys

MAX_START_VAL = 100_000_000

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
        if start_val % (max_val // 20) == 0:
            print(f"Progress: {start_val:,}/{max_val:,} ({start_val / max_val * 100:.2f}%)")
        if collatz_nextval[start_val] != 0:
            # print("Skipping", start_val, "has already stored", collatz_nextval[start_val])
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
        output_str.append(str(i+1) + ": " + str(output[i]))
    return "\n".join(output_str)

def main():
    start = time()
    output = collatz(MAX_START_VAL)
    end = time()
    print("Took", (end - start) / 1e9, "seconds")
    
    output = output[1:]
    output_dir = Path(__file__).parent / "outputs" # Directory for outputs
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = output_dir / f"collatz-{MAX_START_VAL:_}.txt"
    with open(output_path, "w") as f:
        f.write(format_output(output))

    print("Output written to", output_path)

if __name__ == "__main__":
    main()