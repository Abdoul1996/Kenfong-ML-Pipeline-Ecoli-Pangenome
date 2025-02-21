from pathlib import Path
from FastaIndex import FastaIndex
import subprocess
from io import StringIO
import pandas as pd

def align_seq(blast_hits_path:str,
              subject_ref:FastaIndex,
              query_ref:FastaIndex
              ) -> None:
    """
    Align all blast hits
    """

    hit = { #temporary until read loop over blast output or dataframe
        "subject ID": "1",
        "subject start": 406107, 
        "subject end": 405331,
        "query ID": "FAHFDEJI_01155",
        "query start": 1, 
        "query end": 777,
    }
    
    blast_hits = pd.read_csv(blast_hits_path, delimiter='\t')

    alignment_info = []
    current_row = 0
    for index, hit in blast_hits.iterrows():
        print("current row:", current_row, end="\r")
        current_row += 1
        hit : pd.Series

        #check if all the columns are present
        col_set = set(['subject ID', 'subject start', 'subject end', 'query ID', 'query start', 'query end'])
        if not col_set.issubset(hit.index):
            print(f"{hit} has missing columns!")
            print(f"please check input if columns [{", ".join(col_set)}] exist")
            return

        #get the columns
        sub_id = hit.get('subject ID')
        sub_start = hit.get('subject start')
        sub_end = hit.get('subject end')
        query_id = hit.get('query ID')
        query_start = hit.get('query start')
        query_end = hit.get('query end')

        #get subject_ref (sample) sequence
        subject_seq = subject_ref.get_seq(id=sub_id, start=sub_start, end=sub_end)

        #get query_ref (pangenome) sequence
        query_seq = query_ref.get_seq(id=query_id, start=query_start, end=query_end)

        #put sequences into string
        seq_str = ""
        seq_str += f">{sub_id}\n"
        seq_str += subject_seq + "\n"
        seq_str += f">{query_id}\n"
        seq_str += query_seq + "\n"

        #pipe into mafft - adapted from https://mhmmdbduh.medium.com/sequence-alignment-using-mafft-in-python-335a4a84a6d4 
        mafft_subP = subprocess.Popen(['mafft', '--auto', '--quiet', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        mafft_subP.stdin.write(seq_str.encode())
        mafft_out = mafft_subP.communicate()[0].decode('utf8') #get stdout and decode to utf8
        seq_alignment = StringIO(mafft_out).getvalue() #here's the output of mafft!
        mafft_subP.stdin.close()

        #print alignment, and return
        # print(seq_alignment)
        alignment_info.append(take_subject(seq_alignment))
    # return seq_alignment
    print(alignment_info)
    return alignment_info

def take_subject(alignment_str:str) -> tuple[str, str]:
    """Get subject(sample) sequence and query(pangenome) header
        This is to make the sequence identifiable by the header on the pangenome later
        returns (header, sequence)
    """
    align_list = alignment_str.split(">") #split into "genes" - header + sequence chunks
    align_list = [gene for gene in align_list if gene != ""] #remove any empty
    headers = []
    sequences = []
    for gene in align_list:

        lines = gene.split("\n")
        header = ">" + lines[0]
        headers.append(header)
        sequence = "".join(lines[1:])
        sequences.append(sequence)
    return (headers[1], sequences[0])


if __name__ == "__main__":
    #1. Create a blast database from one sample
    #2. Query your pangenome file against the sample to get a blast output file
    #3. Use this align_seq() function as shown below
    #   - index both subject FASTA and query FASTA
    #   - use the function 
    blast_hits_path = "alignment-tests/pang_blast_samples/ERR1218553/pangenome_blast_results.out"   #blast output file from alignment
    subject_ref = FastaIndex("alignment-tests/pang_blast_samples/ERR1218553/assembly.fasta")        #indexed subject FASTA
    query_ref = FastaIndex("pan_genome_reference.fa")                                               #indexed pan genome FASTA
    align_seq(
        blast_hits_path=blast_hits_path,
        subject_ref=subject_ref,
        query_ref=query_ref
        )