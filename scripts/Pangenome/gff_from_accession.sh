#!/bin/bash -l
source /opt/miniconda3/bin/activate base

#loop over lines in a file
while read acc; do
    conda run -n codelab --no-capture-output prefetch $acc 
    conda run -n codelab --no-capture-output fasterq-dump $acc --split-files

    conda run -n codelab --no-capture-output \
        bbduk.sh -Xmx1g in=${acc}_1.fastq in2=${acc}_2.fastq \
            out1=${acc}_trim1.fastq out2=${acc}_trim2.fastq \
            qtrim=r1 trimq=10

    conda run -n unicycler --no-capture-output \
        unicycler -1 ${acc}_trim1.fastq -2 ${acc}_trim2.fastq -o ./unicycler_output/$acc -t 20 --keep 0 --verbosity 1

    conda run -n prokka --no-capture-output \
        prokka ./unicycler_output/${acc}/assembly.fasta --outdir ./prokka_output/$acc --prefix $acc --force
    
    #cleanup prefetch, fasterq-dump, trim, and unicycler temp files
    rm -rf $acc
    rmdir fasterq*
    rm *fastq
    rm -rf ./unicycler_output/$acc
done < $1