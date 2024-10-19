# SAM, BAM, and SAMtools Tool Documentation
### Overview
SAM (Sequence Alignment Map) and BAM (Binary Alignment/Map) are formats used to store sequencing reads that have been aligned to a reference genome. SAM is a text-based format, while BAM is its binary version, making it more efficient for storage and processing. SAMtools is a suite of utilities for manipulating SAM and BAM files, including sorting, indexing, filtering, and creating consensus sequences.

### Functionality
- SAM: Text-based format used to store alignment information.
- BAM: Binary, compressed version of SAM, more efficient for storage and faster to process.
- SAMtools: A collection of utilities for manipulating and analyzing SAM/BAM files, including sorting, indexing, filtering, and creating consensus genomes.

### Installation
You can install SAMtools using Conda or from source.
Conda Installation:
```bash
# Install SAMtools via Conda
conda install -c bioconda samtools
Source Installation:

# Install SAMtools from source
sudo apt-get install samtools
```

### Usage Example

1. Viewing a SAM or BAM File:
To view a SAM or BAM file in a human-readable format:

```bash
# View a SAM file
samtools view alignment.sam
```
```bash
# View a BAM file
samtools view alignment.bam
```

```bash
2. Converting SAM to BAM:
samtools view -S -b alignment.sam > alignment.bam

-S: Input is in SAM format.
-b: Output is in BAM format.
3. Sorting a BAM File:
Sort a BAM file by the reference genome's coordinates:
```
```bash
# Sort BAM file
samtools sort alignment.bam -o sorted_alignment.bam
```
```bash
4. Indexing a BAM File:
#Create an index for a BAM file, making it more efficient to retrieve specific alignments:
samtools index sorted_alignment.bam
```
```bash
# Index BAM file
samtools index sorted_alignment.bam
```

5. Filtering Reads from BAM:
To filter out reads that fail quality checks:

``` bash
# Filter out reads with low mapping quality (e.g., quality < 20)
samtools view -q 20 -b sorted_alignment.bam > filtered_alignment.bam
-q 20: Filters reads with mapping quality less than 20.
```
6. Creating a Consensus Genome:
To create a consensus genome from a BAM or SAM file:

```bash
# Create a consensus genome from BAM file
samtools consensus sorted_alignment.bam > consensus.fasta
This method constructs a single sequence based on multiple aligned reads, reflecting the most common base at each position.

Parameters
view: Used to view or convert between SAM and BAM formats.
sort: Sorts a BAM file by reference coordinates.
index: Indexes a BAM file for fast access.
consensus: Creates a consensus sequence based on aligned reads in a SAM/BAM file.
-q: Quality threshold for filtering reads based on mapping quality.
Output Files
SAM: Text-based alignment file.
BAM: Binary version of SAM, more compact and efficient for storage.
BAI: Index file for a BAM file, used for quick access to specific regions.
FASTA: Consensus sequence output when using samtools consensus.
```

#### Performance
- **Speed** : SAMtools is highly efficient, particularly when working with BAM files, which are faster to process than SAM files.
- **Resource Usage**: Minimal CPU and memory usage for small datasets; resource usage scales with dataset size.

### Notes
SAMtools is essential for any pipeline that involves alignment, as it provides utilities to manipulate and analyze SAM/BAM files efficiently.
BAM files are preferred for downstream processing due to their smaller size and faster processing capabilities compared to SAM files.
The consensus genome method is useful for generating a reference sequence based on the most frequent bases observed at each position across multiple reads.

### Issues/Challenges
- SAM files can be very large, making them impractical for storage and slower for processing. Always convert to BAM format for efficient analysis.
- In low coverage regions, the consensus sequence may not be fully accurate due to the lack of sufficient data at certain positions.

### Link to Documentation
Add later documentation 