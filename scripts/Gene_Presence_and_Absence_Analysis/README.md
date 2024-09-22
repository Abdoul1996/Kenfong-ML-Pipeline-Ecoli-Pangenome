# 🧬 Gene Presence/Absence Analyzer

## Overview of Functions

1. **`print_entire_gene_list`**:  
   Prints all genes along with the count of `1`s (presence) and `0`s (absence) across all samples.

2. **`print_genes_with_less_than_10_ones`**:  
   Filters and prints genes that appear in fewer than 10 samples, i.e., genes with less than 10 occurrences of `1`.

3. **`save_genes_with_less_than_10_ones_to_file`**:  
   Saves the filtered genes (those with less than 10 occurrences of `1`) to a text file. The filename can be specified, otherwise, it defaults to `genes_with_less_than_10_ones.txt`.

## Data Structure

The data is structured in a `pandas.DataFrame`, where:
- **Rows**: Represent different genes.
- **Columns**: Represent samples.
- **Values**: Represent gene presence (`1`) or absence (`0`) in a given sample.

### Example:

| Gene        | ERR4034064 | ERR4034091 | ERR4034111 | ... |
|-------------|------------|------------|------------|-----|
| rplV        | 1          | 1          | 1          | ... |
| group_23205 | 1          | 1          | 1          | ... |
| rplE        | 1          | 1          | 1          | ... |

## Requirements

- **Python** (with Jupyter Notebook support)
- **Pandas** for DataFrame operations

### Install Pandas:
```bash
pip install pandas
