# Snippy Tool Documentation
### Overview
Snippy is a bioinformatics tool used to find SNPs (Single Nucleotide Polymorphisms) and Indels (insertions and deletions) by comparing sequencing reads to a reference genome. It identifies both substitutions (SNPs) and Indels, providing a comprehensive look at the genetic variation between the reference and the sequence data.

### Functionality
- **Purpose**: Detect SNPs and Indels between a reference genome and sequence reads.
- **Input**: FASTQ files (reads) and a reference genome in FASTA format.
- **Output**: VCF (Variant Call Format) file containing the SNPs and Indels, along with other output files for 
visualization and downstream analysis.

### Installation
Snippy can be installed via Conda or from source. The easiest method is through Conda:

```bash
# Install Snippy via Conda
conda install -c bioconda snippy
Alternatively, you can install Snippy from source:
```
```bash
# Clone and install Snippy from GitHub
git clone https://github.com/tseemann/snippy.git
cd snippy
```
### Usage Example
To find SNPs and Indels between sequencing reads and a reference genome:
``` bash
# Run Snippy with paired-end reads and a reference genome
snippy --cpus 4 --outdir snippy_output --ref reference.fasta --R1 acc_1.fastq --R2 acc_2.fastq
In this example:

--cpus: Specifies the number of CPUs to use.
--outdir: Specifies the output directory for results.
--ref: The reference genome in FASTA format.
--R1, --R2: Paired-end FASTQ files (reads).
Parameters
--cpus: Number of CPUs for parallelization.
--outdir: Output directory for Snippy results.
--ref: Reference genome in FASTA format.
--R1, --R2: Paired-end FASTQ files for sequencing reads.
--cleanup: Deletes unnecessary intermediate files to save disk space.
```
Example with additional parameters:

```bash
snippy --cpus 8 --outdir snippy_output --ref reference.fasta --R1 acc_1.fastq --R2 acc_2.fastq --cleanup

### Output Files
- VCF: Variant Call Format file containing SNPs and Indels.
- aln: Alignment file in FASTA format showing the alignment between the reference genome and the reads.
- txt: Summary report of SNPs and Indels found.
- snps.tab: A tab-delimited file listing all detected SNPs.
- The VCF file is the most important output, which can be used for further variant analysis.
```
### Performance
Speed: Snippy is efficient and can be sped up using multiple CPUs.
Resource Usage: Uses moderate memory and CPU, especially when handling large datasets with many variants.

### Issues/Challenges
- Large genetic differences between the reference genome and the reads can result in fewer SNPs being detected.
- Ensure that the quality of the reads is good, as poor-quality reads can lead to false SNP calls. Tools like BBDuK can help clean up reads before running Snippy.

### Link to Documentation
[Snippy GitHub Documentation](https://github.com/tseemann/snippy)

