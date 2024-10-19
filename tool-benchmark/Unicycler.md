# Unicycler Tool Documentation
### Overview
Unicycler is a tool used for genome assembly, combining both short-read and long-read sequencing data. It is primarily used for de novo genome assembly, where the goal is to reconstruct the genome of an organism from raw sequencing reads without the use of a reference genome. Unicycler takes fragmented DNA sequences and pieces them together to form longer contiguous sequences (contigs).

### Functionality
- **Purpose**: Construct a genome assembly from raw sequencing reads.
- **Input**: Short or long sequencing reads in FASTQ format.
- **Output**: Assembled genome in FASTA format.

### Installation
Unicycler can be installed via Conda, Docker, or built from source. The recommended method is through Conda:

```bash
# Install Unicycler via Conda
conda install -c bioconda unicycler
# Install Unicycler via Docker
docker pull staphb/unicycler
```

### Usage Example
To assemble a genome using Unicycler with paired-end short reads:

```bash
# Run Unicycler with paired-end reads
unicycler -1 acc_1.fastq -2 acc_2.fastq -o output_directory

For hybrid assembly (using both short and long reads):
# Run Unicycler with both short and long reads
unicycler -1 acc_1.fastq -2 acc_2.fastq -l long_reads.fastq -o output_directory

Parameters
-1: Input FASTQ file for paired-end read 1.
-2: Input FASTQ file for paired-end read 2.
-l: Input FASTQ file for long reads.
-o: Output directory where the results will be stored.
--min_fasta_length: Minimum length for contigs to be included in the output FASTA file.
```

### Performance
- **Speed**: Depends on dataset size and whether short or hybrid reads are used. Hybrid assembly with long reads may take more time.
- **Resource Usage**: Requires significant CPU and memory, especially for large genomes.

### Notes
- De novo assembly creates longer sequences (contigs) from fragmented reads, which are crucial when no reference genome is available.
- Unicycler can also create circularized contigs, important for certain bacterial genome assemblies.

### Issues/Challenges
- High-quality input data is necessary for accurate genome assembly. Low-quality reads or missing data may result in fragmented assemblies.
- Long-read data greatly improves the assembly of complex or repetitive genomes.
### Link to Documentation
- [GitHub Unicycler Documentation](https://github.com/rrwick/Unicycler)


