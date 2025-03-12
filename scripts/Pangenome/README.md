# 2D Pangenome tools

## Dependencies

- python v3.12
- bbduk (bbmap) v39.01
- unicycler v0.5.0
- prokka v1.14.6
- roary v3.13.0
- samtools v1.18


# Pipeline

Each step is able to be done in succession, but are split into separate tools in order to switch environments in between. Conda can be used to switch between tools by using the `conda run` command. Check conda's docs for more info. 

### Quality control

To quality control your downloaded FASTQ files, one way would be to use fastqc to first generate reports for each FASTQ file:  
`fastqc ./*.fastq` 
    
Then using multiqc to analyze multiple files in a directory:  
`multiqc .`  

### Trimming the Files

The provided `batch_trim.py` script uses bbduk (from bbmap) to trim paired fastq files from an input directory, then outputs the trimmed versions to an output directory. The input files should be paired in the form `ERRXXXXXX_1.fastq` and `ERRXXXXXX_2.fastq`. The output files will be placed in the `<output_directory>` and will be named `ERRXXXXXX_trim1.fastq` and `ERRXXXXXX_trim2.fastq`.  
   
Ex: `python batch_trim.py ./my_directory/fastq_files ./my_directory/trimmed_files/`  

### De-Novo Assembly

Ex: `python batch_unicycler.py ./my_directory/trimmed_files/ ./my_directory/unicycler_files`  

### Genome Annotation

Ex: `python batch_prokka.py ./my_directory/unicycler_files/ ./my_directory/prokka_files/`  

### Pan-Genome Generation
 
Ex: `python batch_roary.py ./my_directory/prokka_files/ ./my_directory/roary_files/`  

### Bowtie indexing

### Consensus Sequence Creation
 
Ex: `python batch_consensus.py ./my_accessions.txt ./my_directory/fastq_files my-bowtie-index`  

# Other tools

These tools do not have any other dependencies other than python3.

### concat_fa.py

This concatenates a FASTA file so that no sequence titles are present. This will not work with FASTQ files.  
  
For example, this FASTA file,  

```ruby
>Sequence1
CATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
>Sequence2
GTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTA
```  

Becomes this when concatenated:  

```ruby
CATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT
GTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTAGTA
```

Ex: `python concat_fa.py ./ERRXXXXXX.fastq`

### get_accessions.py

Gets accession numbers from FASTA files within a directory.    
Ex: `python get_accessions.py ./my_directory/fastq_files/`  

---

#downloading Mills data
mills_data.tsv is a TSV file gotten from the BIOPROJECT PRJNA809394
Link: https://www.ncbi.nlm.nih.gov/datasets/genome/?bioproject=PRJNA809394

5/15/2024
downloaded dataset using ncbi-datasets-cli
command: `datasets download genome accession PRJNA809394 --include genome`

Entire file is est. ~3GB