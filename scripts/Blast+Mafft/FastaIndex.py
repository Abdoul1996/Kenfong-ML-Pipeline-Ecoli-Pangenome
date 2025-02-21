import os


class FastaIndex:
    def __init__(self, fasta):
        """index a FASTA file for easier sequence-getting"""

        if not os.path.isfile(fasta):
            print(f"FILE {fasta} does not exist")

        self._fa_dict = {}
        self._sequence:str = ""

        #read file and split into a list of genes
        with open(fasta, "r") as f:
            genes = f.read().split(">")
        
        self._sequence = "".join([seq for seq in genes if ">" not in seq]).replace("\n", "")

        #put genes into a dictionary _fa_dict
        for gene in genes:
            content = gene.split("\n")
            header = content[0].split(" ")[0]
            sequence = content[1:]

            self._fa_dict[header] = "".join(sequence)
        print(f"loaded {fasta}")
        
    def get_seq(self,id:str, start:int, end:int) -> str:
        """
        Return string sequences from start/end positions, start end end inclusive.
        \nid - id of gene
        \nstart - start index of sequence
        \nend - end index of sequence
        """
        if type(id) is not str:
            id = str(id)

        #handle reverse cases where start is greater than end
        if start > end:
            start, end = end, start #swap start and end
            sequence = self.get_gene(id)[start-1:end]
            return self.reverse_complement(sequence) #return reverse

        return self.get_gene(id)[start-1:end] #start and end inclusive
    
    def get_gene(self, gene_name:str) -> str:
        """Return str sequence if gene exists"""
        if not isinstance(gene_name, str):
            raise TypeError(f"{gene_name} is not a string!")
        return self._fa_dict.get(gene_name)
    
    @staticmethod
    def reverse_complement(sequence:str) -> str:
        """Return reverse complement of a sequence"""
        complement_seq = ""
        complements = {"A":"T", "T":"A", "C":"G", "G":"C"}
        for base in sequence:
            complement_seq += complements[base]
        return complement_seq[::-1] # return the reverse of the complement sequence
    
    @property
    def get_dict(self) -> dict:
        return self._fa_dict
    
    @property
    def keys(self) -> set:
        return self._fa_dict.keys
    

    