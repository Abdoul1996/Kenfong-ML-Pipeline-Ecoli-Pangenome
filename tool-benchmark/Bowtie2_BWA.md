# Bowtie, Bowtie2, and BWA Tool Documentation
### Overview
Bowtie and Bowtie2 are tools used for aligning sequencing reads to a reference genome or pangenome. Bowtie is designed for short-read alignments, while Bowtie2 improves on this by supporting longer reads and gapped alignments. BWA (Burrows-Wheeler Aligner) is another popular tool for aligning sequencing reads to a reference genome, known for its accuracy and speed. All three tools output alignments in the SAM format, which can be further processed into BAM format using tools like SAMtools.

### Functionality
**Bowtie**: Fast aligner for short reads.
**Bowtie2**: Improved aligner for longer reads and gapped alignments.
**BWA**: Accurate aligner, handles both short and long reads, and supports gapped alignments.

- Input: FASTQ files (reads) and a reference genome in FASTA format.
- Output: Alignments in SAM format.

### Installation
All three tools can be installed via Conda or from source.

Bowtie2 and Bowtie Installation:
```bash
# Install Bowtie2 via Conda
conda install -c bioconda bowtie2
Alternative, install from source:
# Install Bowtie2 from source
sudo apt-get install bowtie2
```

BWA Installation:
```bash
# Install BWA via Conda
conda install -c bioconda bwa
Alternatively, install from source:
# Install BWA from source
sudo apt-get install bwa
```

### Usage Examples
Bowtie2 Example:
- To align paired-end reads to a reference genome using Bowtie2:

``` bash
# Build an index from the reference genome
bowtie2-build reference.fasta reference_index

# Align paired-end reads to the reference genome
bowtie2 -x reference_index -1 acc_1.fastq -2 acc_2.fastq -S output.sam
```
### Explanation:
- bowtie2-build: Creates an index from the reference genome.
- -x: Reference genome index file.
- -1, -2: Paired-end FASTQ files.
- -S: Output SAM file.

BWA Example:
To align paired-end reads using BWA:

```bash
# Index the reference genome
bwa index reference.fasta

# Align paired-end reads to the reference genome
bwa mem reference.fasta acc_1.fastq acc_2.fastq > output.sam
```
Explanation:
- bwa index: Indexes the reference genome.
- bwa mem: Aligns paired-end reads.
- >: Redirects the output to a SAM file.

Bowtie Example (for shorter reads):
```bash
# Build an index from the reference genome
bowtie-build reference.fasta reference_index

# Align single-end reads to the reference genome
bowtie -x reference_index acc.fastq -S output.sam

Parameters
For Bowtie2 and BWA, key parameters include:

-x (Bowtie2): Reference genome index prefix.
-1, -2: FASTQ files for paired-end reads.
-S: Output file in SAM format.
--very-sensitive (Bowtie2): Ensures highly sensitive alignment, sacrificing speed for accuracy.
-p: Number of threads for parallel processing.
mem (BWA): Used for aligning paired-end reads.
```

### Output Files
- SAM: Sequence Alignment/Map format (text-based alignment output).
- BAM: Binary version of SAM (more compact and easier to manipulate).
- Index Files: Generated from the reference genome and used for fast lookups during alignment.

### Performance
- Bowtie2: Optimized for speed and performs well with long-read alignments and gapped alignments.
- BWA: Known for its high accuracy and handles both short and long reads.
- Bowtie: Extremely fast for short-read alignments, but less flexible than Bowtie2 and BWA.

### Notes
Bowtie2 is ideal for projects involving long-read sequencing, and for those needing gapped alignments.
BWA is well-suited for handling complex alignments and works well with both short and long reads.
Bowtie is the tool of choice when speed is the highest priority and reads are short, but consider Bowtie2 or BWA for more accuracy and flexibility.
Both Bowtie2 and BWA output in SAM format, which can be converted to BAM format using SAMtools for further processing.

### Issues/Challenges
- Large reference genomes may require significant memory and time for indexing.
- Ensure that reads are properly trimmed (use tools like BBDuK) for better alignment quality.
- Alignment parameters need fine-tuning depending on the dataset (especially --very-sensitive for Bowtie2).

### Link to Documentation

Myco and Estafenos can you add the documentation here I could not find them 
[Bowtie2 Documentation]()
[BWA Documentation]()