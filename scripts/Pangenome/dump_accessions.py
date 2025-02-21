
import argparse
import subprocess
from pathlib import Path

#Myco Torres
#SFSU 2023
#CoDE Lab

# Downloads multiple isolates using fasterq-dump and a text file containing accession id's
# Checks if isolate is already downloaded

# Usage: python dump_accessions <accessions.txt> <output_directory>

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="dump_accessions.py",
    )
    parser.add_argument("accession_txt")
    parser.add_argument('out_dir')
    return parser.parse_args()

def main(args :argparse.Namespace):
    #Make output path exist
    output_dir = Path(args.out_dir)
    output_dir.mkdir(exist_ok=True)
    
    #get all filenames in ouput directory
    file_list = list(output_dir.glob("*_1.fastq"))
    file_list = [x.name for x in file_list]  
    
    with open(args.accession_txt, "r") as f:
        for acc in f:
            #check if text file accession number is in output directory
            if f"{acc.strip()}_1.fastq" not in file_list:
                print(f"fasterq-dump -p {acc.strip()} -O {output_dir}")
                subprocess.run(f"fasterq-dump -p {acc.strip()} -O {output_dir}", shell=True)

if __name__ == "__main__":
    args = get_args()
    main(args)
    quit()