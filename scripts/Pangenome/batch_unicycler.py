

import argparse
from pathlib import Path
import subprocess

#Myco Torres
#SFSU 2023
#CoDE Lab

#Usage: python uni.py
#Ex: python uni.py

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="uni.py",
        description="Run unicycler on all accessions in a directory"
    )
    parser.add_argument("input_directory")
    parser.add_argument("output_directory")
    return parser.parse_args()

def main(args: argparse.Namespace):
    input_path = Path(args.input_directory)
    output_path = Path(args.output_directory)
    output_path.mkdir(exist_ok=True)
    
    for file_path in input_path.iterdir():
        file_name = file_path.name
        
        if "trim1" in file_name:
        
            file_root = file_name.split("_")[0]
            forward_file = file_root + "_trim1.fastq"
            reverse_file = file_root + "_trim2.fastq"
        
            subprocess.run(f"unicycler -1 {input_path/forward_file} -2 {input_path/reverse_file} -o {output_path/file_root}",
                           shell=True)
    


if __name__ == "__main__":
    args = get_args()
    main(args)
    quit()