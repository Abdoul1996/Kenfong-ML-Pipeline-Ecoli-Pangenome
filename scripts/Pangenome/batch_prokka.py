
import argparse
from pathlib import Path
import subprocess

#Myco Torres
#SFSU 2023
#CoDE Lab

#Usage: python prok.py
#Ex: python prok.py


def get_args():
    parser = argparse.ArgumentParser(
        prog="prok.py",
        description="Run Prokka on all files in a directory"
    )
    parser.add_argument("input_directory")
    parser.add_argument("output_directory")
    
    return parser.parse_args()

def main(args):
    input_path = Path(args.input_directory)
    output_path = Path(args.output_directory)
    output_path.mkdir(exist_ok=True)
    
    #Check if input dir is a dir
    if not input_path.is_dir():
        print(f"Input '{args.input_directory}' is not a directory!")
        quit()
    
    #loop through acc
    for acc_path in input_path.iterdir():
        #check if acc doesn't exist in prokka output directory
        subprocess.run(f"prokka {acc_path}/assembly.fasta --outdir {output_path/acc_path.name} --prefix {acc_path.name}", shell=True)

if __name__ == "__main__":
    args = get_args()
    main(args)
    quit()