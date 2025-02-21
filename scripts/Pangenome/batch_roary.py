
import argparse
import subprocess
from pathlib import Path

#Myco Torres
#SFSU 2023
#CoDE Lab

#Usage: python batch_roary.py <input_directory> <output_directory>

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog = "batch_roary.py",
        description= "Creates pan-genome from gff files in directory"
    )
    parser.add_argument("input_directory")
    parser.add_argument("output_directory")
    return parser.parse_args()

def main(args: argparse.Namespace):
    input_path = Path(args.input_directory)
    output_path = Path(args.output_directory)
    
    subprocess.run(f"roary -e --mafft -v -p 8 -f {output_path} {input_path/'*/*.gff' }", shell=True)

if __name__ == "__main__":
    args = get_args()
    main(args)
    