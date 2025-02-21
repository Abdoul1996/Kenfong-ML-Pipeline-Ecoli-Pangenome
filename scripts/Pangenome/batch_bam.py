
import pathlib
import subprocess

#inputs
bowtie_index = ""
input_dir = ""
output_dir = ""

def get_accs(input_dir):
    #create a set to prevent duplicates
    acc_set = set()
    acc_path = pathlib.Path(input_dir)
    
    #loop over files in fasta_dir
    for x in acc_path.iterdir():
        
        #if it contains FASTA/FASTQ/FA
        if "fa" in x.name.lower():
            
            #split name by dots and underscores, then get first item from resulting list
            acc = x.name.split(".")[0].split("_")[0]
            acc_set.add(acc)
    
    return sorted(acc_set) 

def create_bam(accession_list, output_dir):

    for acc in accession_list:
        print(f"bowtie2 -x bowtie index -U {acc}, {acc} | samtools view -bS - > {output_dir}/{acc}.bam")
        # subprocess.run(f"bowtie2 -x bowtie index -U trim1, trim2 | samtools view -bS - > out.bam")
        #sort bam
    
if __name__ == "__main__":
    accs = get_accs(input_dir)
    create_bam(accs, output_dir = output_dir)
    