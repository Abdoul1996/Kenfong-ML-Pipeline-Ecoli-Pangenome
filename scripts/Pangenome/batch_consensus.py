

import argparse
import os
import subprocess
import time

# Myco Torres
# SFSU 2023
# CoDE Lab

#usage: python batch_consensus.py  accession_txt  data_dir  bowtie_index
#creates file ERXXXXXX.consensus.fa

#TODO make script simpler
# have only data dir as input
# automatically create bowtie2 index
# remove time stamp

def load_args():
    """Load arguments from command-line"""
    parser = argparse.ArgumentParser(
        prog = "batch_consensus",
        description = """Batch create consensus sequences from FASTQ/FASTA files """
    )
    parser.add_argument('accession_txt', help="""A text file containing accession numbers to create consensus sequences from.""")
    parser.add_argument('data_dir', help="Directory that contains forward and reverse FASTA/FASTQ files")
    parser.add_argument('bowtie_index', help = "Bowtie index to be used")
    parser.add_argument('--threads', help = "Number of threads to be used. default = 4", default=4)
    return parser.parse_args()

def main(accession_txt, bowtie_index, num_threads, data_dir):
    accessions = [line.strip() for line in open(accession_txt, 'r').readlines()]
    accessions = [line for line in accessions if line != ""]
    
    #loop over accessions
    for acc in accessions:
        print(f">>> Starting {acc}")
        if not create_consensus(acc, bowtie_index, num_threads, data_dir):
            print(f"XXX {acc} failed, skipping...")
        break
    
def create_consensus(acc, bowtie_index, num_threads, data_dir):

    print(" -> Trimming files ...")
    subprocess.run(f"bbduk.sh -Xmx1g in1={data_dir+acc}_1.fastq in2={data_dir+acc}_2.fastq out1={acc}_trim1.fastq out2={acc}_trim2.fastq qtrim=rl trimq=10", shell=True)
    
    print(" -> Creating sam file...")
    subprocess.run(f"bowtie2 -x {bowtie_index} -p {num_threads} -U {acc}_trim1.fastq, {acc}_trim2.fastq -S {acc}.sam", shell=True)

    print(" -> Sorting file...")
    subprocess.run(f"samtools sort -o {acc}.sam {acc}.sam", shell=True)
    
    print(" -> Creating consensus file...")
    subprocess.run(f"""samtools consensus --show-del yes --show-ins no -m "simple" -aa -@ {num_threads} -o {acc}.consensus.fa {acc}.sam""", shell=True)
    
    print(" -> Removing leftover files...")
    subprocess.run(f"rm {acc}.sam", shell=True)
    

def cleanup(directory):
    if "sam" in os.listdir(directory):
        subprocess.run(f"rm *sam*", shell=True)
        
def get_duration(start_time, end_time):
    duration = end_time - start_time
    min, sec = divmod(duration ,60)
    hr, min = divmod(min, 60)
    return int(hr), int(min), int(sec)
    

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    args = load_args()
    start_time = time.time()
    try:
        main(
            accession_txt = args.accession_txt,
            bowtie_index = args.bowtie_index,
            num_threads= args.threads,
            data_dir= args.data_dir,
        )
    finally:
        cleanup(current_dir)
    end_time = time.time()
    
    hr, min, sec = get_duration(start_time, end_time)
    print(f"Took {hr} hrs {min} mins {sec} secs")
    exit(0)
    