import os 

dir = "./reference_genes/"
files = os.listdir(dir)

csv_filename = "gene_lengths_3_dataset_pangenome.csv"

with open(csv_filename, "w") as f:
    for file in files:
        #open each file and count how many letters
        with open(dir+file, "r") as g:
            lines = g.readlines()[1:]
            lines = [lin.strip() for lin in lines]
            lines = "".join(lines)
            length = len(lines)
            print(length)
        
        f.write(file.split(".")[0] + "\t" + str(length) + "\n")
