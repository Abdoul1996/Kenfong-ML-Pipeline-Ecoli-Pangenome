# Prokka Tool Documentation
### Overview
Prokka is a rapid genome annotation tool specifically designed for annotating bacterial, archaeal, and viral genomes. It identifies and labels features such as genes, coding sequences (CDS), rRNA, tRNA, and other elements within a genome. Prokka outputs annotated genomes in standard formats like GFF and GenBank.

### Functionality
- **Purpose**: Annotate genomes by identifying genes, coding sequences, and other genomic features.
- **Input**: Assembled genome in FASTA format.
- **Output**: Annotated genome in GFF, GenBank, and other formats.

### Installation
Prokka can be installed using Conda or from source. The easiest way is through Conda:

```bash
# Install Prokka via Conda
conda install -c bioconda prokka
alternative: 
# Clone and install Prokka from GitHub
git clone https://github.com/tseemann/prokka.git
cd prokka
make
```
### Usage Example
To annotate a genome:
```bash
# Run Prokka on an assembled genome
prokka assembled_genome.fasta --outdir annotation_output --prefix sample_name
This command will annotate the genome in assembled_genome.fasta and save the results in the annotation_output directory. The output files will be prefixed with sample_name.

Parameters
--outdir: Specifies the output directory.
--prefix: Prefix for the output files.
--cpus: Number of CPUs to use for faster processing.
--genus: Genus name for more specific annotation.
--kingdom: Specify the kingdom (Bacteria, Archaea, or Viruses).
```
### Output Files
Prokka generates multiple output files:

- gff: General Feature Format file, containing all annotations.
- gbk: GenBank format file with detailed annotations.
- faa: FASTA file with protein sequences of identified CDS.
- ffn: FASTA file with nucleotide sequences of CDS.
- fna: FASTA file with the contig sequences.
- txt: Summary report of the annotation.

### Performance
- **Speed**:Prokka is optimized for speed and can handle large bacterial genomes within minutes.
- **Resource Usage**: Can be optimized using multiple CPUs.

### Issues/Challenges
- Misannotations can occur if the genome quality is poor or if genus/kingdom is not specified.
For large or complex genomes, manual curation may still be necessary.
### Link to Documentation
- [GitHub Prokka Documentation](https://github.com/tseemann/prokka)