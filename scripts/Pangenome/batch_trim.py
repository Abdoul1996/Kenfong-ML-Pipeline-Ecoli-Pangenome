
import argparse
from pathlib import Path
import subprocess

#Myco Torres
#SFSU 2023
#CoDE Lab

#Usage: python batch_trim.py <input_dir> <output_dir>
#Ex:    python batch_trim.py

#TODO: Make script work with only single

def get_args():
    parser = argparse.ArgumentParser(
        prog="batch_trim_fastq.py",
        description="Trims a directory FASTA/Q files using bbduk. Only works with paired reads ex: acc_1.fa acc_2.fa"
    )
    parser.add_argument("input_directory")
    parser.add_argument("output_directory")
    return parser.parse_args()

def main(args):
    input_dir = Path(args.input_directory)
    out_dir = Path(args.output_directory)
    out_dir.mkdir(exist_ok=True)
    
    #loop over files in input_directory
    for file in input_dir.iterdir():

        if "_1.fastq" in file.name:
            acc = file.name.split("_")[0]
            
            subprocess.run(" ".join([f"bbduk.sh -Xmx1g",
                    f"in1={input_dir/acc}_1.fastq",
                    f"in2={input_dir/acc}_2.fastq",
                    f"out1={out_dir/acc}_trim1.fastq",
                    f"out2={out_dir/acc}_trim2.fastq", 
                    f"qtrim=rl",
                    f"trimq=10"
                    ]), shell=True)
        
    

if __name__ == "__main__":
    args = get_args()
    main(args)
    quit()