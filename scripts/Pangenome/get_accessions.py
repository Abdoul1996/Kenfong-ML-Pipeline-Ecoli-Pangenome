import pathlib
import argparse

#Myco Torres
#SFSU 2023
#CoDE Lab

# Get accession numbers from FASTA files in a directory
# Usage: python get_accessions.py <directory_path> --output <save_dir>
# Ex:    python get_accessions.py ./my_directory --output ../other_directory/accessions.txt

def get_args():
    parser = argparse.ArgumentParser(
        prog = "get_accessions.py", 
        description= "Get accession numbers a directory containing large numbers of FASTA files. "
    )
    parser.add_argument("fasta_dir", help="directory containing FASTA?/FASTQ/FA files")
    parser.add_argument("--output", help="File to save list of accessions. Default: <./accession_list.txt>", default="./accession_list.txt")
    return parser.parse_args()

def main(args):
    
    #create a set to prevent duplicates
    acc_set = set()
    acc_path = pathlib.Path(args.fasta_dir)
    
    #loop over files in fasta_dir
    for x in acc_path.iterdir():
        
        #if it contains FASTA/FASTQ/FA
        if "fa" in x.name.lower():
            
            #split name by dots and underscores, then get first item from resulting list
            acc = x.name.split(".")[0].split("_")[0]
            acc_set.add(acc)
    
    #sort by name
    acc_set = sorted(acc_set) 
    
    #write acc to file
    with open(args.output, "w") as f:
        for y in acc_set:
            f.write(y+"\n")

    print(len(acc_set), "Accessions written to", "\"" + args.output + "\"")

if __name__ == "__main__":
    args = get_args()
    main(args)
    quit()