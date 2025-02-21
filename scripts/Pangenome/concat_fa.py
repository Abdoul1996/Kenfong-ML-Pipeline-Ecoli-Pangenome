
from argparse import ArgumentParser
from pathlib import Path

#Myco Torres
#SFSU 2023
#CoDE Lab

#Usage: concat.py <file> --output <output_filepath>
#Ex:    concat.py ./my_file.fa --output ./my_file.concat.fa

def get_args():
    parser = ArgumentParser(prog = "concat.py",
                            description = "Takes FASTA/FASTQ files and removes sequence name")
    parser.add_argument("in_file", help="File to concatenate")
    parser.add_argument("-o", "--out_dir", help="Output filepath. Default: ./", dest="out_dir", default="./")
    parser.add_argument("-l", "--line_length", help="Length of lines in concatenated file. Default: 80", dest="line_length", default=80)
    
    return parser.parse_args()
    
def main(args):
    
    #str for lines
    seq_str = ""
    acc = f"{Path(args.in_file).name.split('.')[0]}.concat.fa"
    output_path = Path(args.out_dir) / acc
    
    #open file
    with open(args.in_file, "r") as f:
        for line in f:
            if not ">" in line:
                seq_str += line.strip()
        
    with open(output_path, "w") as f:
        for x in range(args.line_length, len(seq_str), args.line_length):
            f.write(seq_str[x-args.line_length: x] + "\n")
    
    print(f"Written to {output_path}")


if __name__ == "__main__":
    args = get_args()
    main(args)
    quit()