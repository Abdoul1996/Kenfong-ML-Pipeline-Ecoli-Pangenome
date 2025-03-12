# Blast+Mafft alignment pipeline

- [FastaIndex](#fastaindex)
- [MutFinder](#mutfinder)


## Dependencies
- python v3.12
- mafft v7.505 (2022/Apr/10)
- pandas v2.2.3

## FastaIndex
FastaIndex is a helper class used to help make retrieving sequences using `start` and `end` indices from BLAST hits easier. 

It does this by parsing FASTA file it is initialized with, and creating a dictionary where the keys are the FASTA headers and the values are sequences. 

```python
from FastaIndex import FastaIndex
fasta_indexed_file = FastaIndex("testfile.fasta")
```

There are a couple of useful methods as part of the FastaIndex class, but the most useful is `FastaIndex.get_seq()`, as the id, start, and end from a blast hit can be used to retrieve a sequence.

Example:

```python
fasta_indexed_file.get_seq(
    id="NFNHAPOA_00300_group_610",
    start=1,
    end=579
)
#returns the sequence at that position of length 579 from the fasta 'NFNHAPOA_00300_group_610'
```

## MutFinder
Mutfinder has a collection of functions that help aligning sequences easier. 

`align_seq()` takes in a `blast_hits.out` file and two related `fasta_indexed` files as input, and aligns all hits within the `blast_hits.out` file. 

It returns a List of tuples(header, sequence) where header is a FASTA header, and sequence is the aligned subject sequence.

```python
from MutFinder import align_seq

blast_hits_path = "path to a list of hits from BLAST"
subject_ref = FastaIndex("path to FASTA")   #Fasta must correspond to the "subject" in the blast hit
query_ref = FastaIndex("path to FASTA")     #Fasta must correspond to the "query" in blast hit

align_seq(
    blast_hits_path = blast_hits_path,
    subject_ref = subject_ref,
    query_ref = query_ref
)
```

# Generating blast Database




# Unused Scripts
These scripts are unused because you can just blast one FASTA file against a blast database instead of separately
- `batch_blast.py` - blasts each gene from a directory to a database
- `split_fasta_to_fsa.py` - splits fasta into separate files
- `cat_blast_results.py` - takes blast results and concatenates results
- `brad_methods.py` - performs all three functions above in succession