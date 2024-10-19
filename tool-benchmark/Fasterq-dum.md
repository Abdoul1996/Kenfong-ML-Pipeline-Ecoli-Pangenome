# Fasterq-dump Tool Documentation
### Overview
Fasterq-dump is a tool from the SRA toolkit that extracts sequencing reads from downloaded SRA data. It outputs paired-end reads as two separate FASTQ files (acc_1.fastq and acc_2.fastq), which are necessary for downstream analysis such as genome assembly or read mapping.

### Functionality
- **Purpose**: Extract FASTQ files from downloaded SRA data.
- **Input**: .sra file downloaded using Prefetch.
- **Output**: Paired-end reads as two FASTQ files: acc_1.fastq and acc_2.fastq.

### Installation
If you've already installed the SRA Toolkit (as shown in the Prefetch example), you already have access to Fasterq-dump. No additional installation steps are needed.

Usage Example
To extract paired-end FASTQ files from an SRA file:

```bash
# Extract paired-end reads from SRA file
fasterq-dump ERR4035812

This command will output two FASTQ files:
- ERR4035812_1.fastq (paired-end read 1)
- ERR4035812_2.fastq (paired-end read 2)

Parameters
--split-files: Outputs the paired-end reads into separate FASTQ files (acc_1.fastq and acc_2.fastq).
--threads: Specifies the number of threads to use, improving performance with large datasets.

fasterq-dump --split-files --threads 4 ERR4035812
```
### Performance
**Speed**: Faster than the older fastq-dump tool.
**Resource Usage**: Memory and CPU usage increase with the size of the dataset.

### Strengths 
Easy to integration with SRA download 
### Weakness 
May require computational resources for large files 
Myco and Estafenos 

### Issues/Challenges
Large datasets may require significant disk space to store the output FASTQ files.
If disk space is a limitation, you can set up output directories using the --outdir flag.

Estefanos and Myco share more here 

### Link Documentation 
[Fasterq-dum](https://github.com/ncbi/sra-tools)
[Prefech and Fasterq-dum](https://github.com/ncbi/sra-tools/wiki/08.-prefetch-and-fasterq-dump)
