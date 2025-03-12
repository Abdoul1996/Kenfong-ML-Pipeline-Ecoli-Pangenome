import os
# from pathlib import Path
import subprocess
from multiprocessing import Pool

input_dir = "reference_genes/"
output_dir = "pan_genome_blast_results/"
os.makedirs(output_dir, exist_ok=True)
db = "pan_genome_reference"

files = os.listdir(input_dir)
num_files = len(files)
processed_files = 0

# for file in files:
#     input_path = f"\'{input_dir+file}\'"
#     output_path = f"\'{output_dir+file.replace('.fsa', '.out')}\'"

#     if os.path.exists(output_path):
#         processed_files += 1
#         continue
#     command = f"blastn -db {db} -query {input_path} -out {output_path} -outfmt \"6\""
#     subprocess.run(command,shell=True)
#     processed_files+=1
#     print(f"{processed_files}/{num_files}", end="\r")

def blast(db, query, output):
    command = f"blastn -db {db} -query {query} -out {output} -outfmt \"6\""
    # print("\t" + command)
    subprocess.run(command, shell=True)
    
num=0
for file in files:
    command = f"blastn -db {db} -query {input_dir+file} -outfmt 6 >> pipe_result.txt"
    subprocess.run(command, shell=True)
    num += 1
    print(num)
