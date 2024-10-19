# BBDuK Tool Documentation
### Overview
BBDuK (BBmap's Decontamination Using K-mers) is a versatile tool used for trimming and filtering sequencing data. It can remove low-quality bases, trim adapters, and filter contaminants from sequencing reads, making it an essential step in preprocessing raw data before assembly or alignment.

### Functionality
- **Purpose**: Trim low-quality bases and filter contaminants from sequencing reads.
- **Input**: Paired-end FASTQ files (acc_1.fastq, acc_2.fastq).
- **Output**: Cleaned FASTQ files with low-quality bases and adapters removed.

### Installation
BBDuK is part of the BBTools suite. You can download BBTools, which includes BBDuK, from the official site or GitHub.

### To install BBTools:

```bash
# Download BBTools (Linux example)
wget https://sourceforge.net/projects/bbmap/files/BBMap_38.90.tar.gz
tar -xvzf BBMap_38.90.tar.gz
cd bbmap
```
### Usage Example
- To trim low-quality bases from paired-end reads:

```bash
# Trim low-quality bases and adapters from paired-end reads
bbduk.sh in1=acc_1.fastq in2=acc_2.fastq out1=trimmed_1.fastq out2=trimmed_2.fastq qtrim=r trimq=10
This command trims low-quality bases from the right end of the reads (qtrim=r) and uses a quality threshold of 10 (trimq=10).
# Trim low-quality bases and adapters from paired-end reads
bbduk.sh in1=acc_1.fastq in2=acc_2.fastq out1=trimmed_1.fastq out2=trimmed_2.fastq qtrim=r trimq=10

Parameters
in1: Input FASTQ file for paired-end read 1.
in2: Input FASTQ file for paired-end read 2.
out1: Output trimmed FASTQ file for paired-end read 1.
out2: Output trimmed FASTQ file for paired-end read 2.
qtrim=r: Trims bases from the right end of reads.
trimq=10: Sets a quality threshold of 10 for trimming.
```

### Performance
- **Speed**: Efficient for large datasets, can handle high-throughput sequencing data.
- **Resource Usage** : Memory usage depends on the size of the dataset and k-mer size.
Myco and Estefanos add details here 

### Issues/Challenges
Incorrect parameter tuning may lead to over-trimming of reads, reducing data quality. Experiment with different quality thresholds and k-mer sizes for optimal results.

### Link to Documentation
[BBDuK Documentation](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbduk-guide/)

