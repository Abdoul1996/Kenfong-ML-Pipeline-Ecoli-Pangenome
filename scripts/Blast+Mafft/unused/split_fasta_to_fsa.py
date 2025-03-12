
import os
reference_file = "pan_genome_reference.fa"
output_dir = "reference_genes"
os.makedirs(output_dir, exist_ok=True)
#refenrence needs to be split once

with open(reference_file, "r") as f:
    gene = ""
    for line in f:
        if ">" in line:
            if gene:
                with open(output_dir+"/"+header+".fsa", "w") as g:
                    g.write(gene)

            header = line.replace(">", "").replace(" ", "_").strip()
            gene = line
        else:
            gene += line

    with open(header+".fsa", "w") as g:
        g.write(gene)





