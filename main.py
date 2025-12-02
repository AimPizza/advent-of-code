import argparse
import subprocess
import os

parser = argparse.ArgumentParser()
parser.add_argument('pos_arg', type=str, help='the number of this years problem')
args=parser.parse_args()

solution_path = f"{args.pos_arg}/main.py"
if not os.path.exists(solution_path):
    print(f"Error: {solution_path} does not exist")
    exit(1)

try:
    result = subprocess.run(
        ["python", os.path.basename(solution_path)],
        cwd=os.path.dirname(solution_path), # ensure working directory of that script
        capture_output=True,
        text=True,
        check=True # exception on non-zero exit
    )
    print(f"solution for {args.pos_arg}: {result.stdout}")
except subprocess.CalledProcessError as e:
    print(f"Error: {e.stderr}")



