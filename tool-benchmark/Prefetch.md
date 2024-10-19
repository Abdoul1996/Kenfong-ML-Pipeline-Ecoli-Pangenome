# Prefetch Tool Documentation
### Overview
Prefetch is a tool from the SRA toolkit used to download raw sequence data from NCBI’s Sequence Read Archive (SRA) by providing an accession number. It is essential for retrieving the initial dataset required for downstream bioinformatics analysis.

### Functionality
- **Purpose**: Download raw sequencing data from the SRA database.
- **Input**:  SRA file => Accession number (e.g., ERR4035812, SRR123456).
- **Output**: SRA file(s) containing the raw sequence data.

### To install Prefetch as part of the SRA toolkit:

```bash
# Install SRA Toolkit (Linux example)
sudo apt-get install sra-toolkit

# Check installation
vdb-config --interactive

# Update PATH (if needed)
export PATH=$PATH:/path/to/sratoolkit/bin
```

### Usage Example 

Download sequence data using an accession number:

```bash
# Download data for a specific accession number
prefetch ERR4035812
# Download data with specific max-size to ouput directory
prefetch ERR4035812 --max-size 20GB --output-directory ./data
```
### Strengths 
- Effecient for downloading large datasets 
### Weaknesses 
- Prefetch downloads .sra files, which need further processing with tools like fasterq-dump to extract the sequencing reads in FASTQ format.

# Myco and Estefanos can add something here

### Performance 
- **Speed**: 
- **Resources Usage**: 
Myco and Estefanos can share the performance 

### Issues/Challenges
Myco share your experiences 

### Link to Documentation
[Prefetch SRA Toolkit Documentation](https://github.com/ncbi/sra-tools)
[Prefetch and Fasterq-dum](https://github.com/ncbi/sra-tools/wiki/08.-prefetch-and-fasterq-dump)

### Example Output
```bash
$ prefetch ERR4035812
Downloading ERR4035812...
Downloading file 'ERR4035812' to local cache: complete.
```
