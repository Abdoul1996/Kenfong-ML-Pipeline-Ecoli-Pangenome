
import os
import subprocess
from multiprocessing import Pool
from pathlib import Path

cwd = Path.cwd()
#1. Split one reference file into multiple .fsa files (or use a pre-existing)
#2. Create a BLAST database out of one sample
#3. BLAST all .fsa files onto reference
#       - use some type of multiprocessing to speed blast up
#4. Concatenate BLAST hits into one file

#Myco T CodeLab 2024

def split_reference(reference_path, output_dir=cwd/"reference_genes"):
    """Spits a reference file via >"""
    #create output dir
    Path(output_dir).mkdir(exist_ok=True)

    with open(reference_path, "r") as f:
        #split up file by ">" first
        #loop over lists
        for gene in f.read().split(">"):
            if not gene:
                continue
            #Split file by newline
            gene = gene.split("\n")
            output_filename = gene[0].replace(" ", "_") + ".fsa"
            header = ">" + gene[0] + "\n"
            
            #write files to output
            with open(output_dir/output_filename, "w") as g:
                g.write(header)
                g.write("\n".join(gene[1:]))

def make_blastdb(database_fasta:Path, database_name:str):
    """
    create a fasta
    database_fasta - PATH of fasta file
    database_name - name of the database to be created. (default: database_fasta stem)
    """
    if not database_name:
        database_name = database_fasta.stem
    subprocess.run(
        f"makeblastdb -in {database_fasta} -dbtype nucl -out {database_name}",
        shell=True,
    ).check_returncode()

def batch_query_blastdb(query_path:Path, database:str, hits_output_path, processes=1 ):
    """
    query_path - A directory containing .fsa files
    database - A path to a BLAST database
    hits_output_path - A path to put all the hits from files
    """
    #find all files in input path and put it into list of [database, query, hits_path]
    query_args = [(database, query, hits_output_path) for query in query_path.iterdir()]
    print(query_args)
    with Pool(processes=processes) as p:
        p.starmap_async(_query_blastdb, query_args)

def _query_blastdb(database, query, output_path):
    subprocess.run(
        f"blastn –db {database} –query {query} –out {output_path} -outfmt 6",
        shell=True
    ).check_returncode()

def cat_query(input_dir:Path, output_file:Path):
    """Query blast database"""
    input_dir.is_dir()
    files = os.listdir(input_dir)

    with open(output_file) as out:
        #write headers first
        out.write('query ID\tsubject ID\tpercent identity\talignment length\tmismatches\tgap opens\tquery start\tquery end\tsubject start\tsubject end\te-value\tbit score\n')
        for file in files:
            path = input_dir+ file
            name = file.replace(".out", "")
            
            #loop over lines in file, and write in output
            with open(path, "r") as g:
                lines = g.readlines()
                if lines:
                    for line in lines:
                        line = line.split("\t")
                        line[0] = name
                        line = "\t".join(line)
                        out.write(line)


if __name__ == "__main__":

    reference_path = "/home/922347787/Myco/brad-method-test/scripts/test_data/test_reference_genome.fa"
    split_reference(
        )