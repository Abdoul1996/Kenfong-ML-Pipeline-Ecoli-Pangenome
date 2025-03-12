#! /bin/bash

#Myco Torres
#SFSU 10/26/23
# usage: batch_consensus.sh <accession.txt> <bowtie_index> <data_dir> <optional: threads>

#requires bbduk bbmap 
#requires bowtie2 
#tested samtools v1.18

accession_txt=$1 
bowtie_index=$2
data_dir=$3
num_threads=${4:-12} #get input 4, otherwise value is 12

declare -i err=0
#check if the text file and data_dir are valid
if [ ! -f "$accession_txt" ] ; then  #if accession is not a file
    echo "ERROR: ${accession_txt} is not a file"
    ((err++))
elif [ ! -d "$data_dir" ] ; then #if data_dir is not a directory
    echo "ERROR: ${data_dir} is not a directory"
    ((err++))
fi

#if errors are greater than 1, exit the program
if [ $err != 0 ] ; then
    echo "usage: batch_consensus.sh <accession.txt> <bowtie_index> <data_dir> <optional: threads>"
    echo " - <accession.txt> text file containing accession numbers - ex. a list of ERRXXXXXX"
    echo " - <bowtie_index> index name created by bowtie-build"
    echo " - <data_dir> directory containing the fasta files - ex. KallonenFastqFiles"
    echo " - <threads> thread count - default 4."
    exit 1
fi

while read acc ; do
    #stops from running newlines in loop
    if [ "$acc" ] && [ ! -f "${acc}.consensus.fa" ] ; then
        echo "Starting $acc"

        echo ">>> Trimming Files..."
        bbduk.sh -Xmx1g in1="${data_dir}""${acc}"_1.fastq in2="${data_dir}""${acc}"_2.fastq \
                        out1="${acc}"_trim1.fastq out2="${acc}"_trim2.fastq \
                        qtrim=rl trimq=10

        echo ">>> Aligning Trimmed fastas to reference genome..."
        bowtie2 -x "${bowtie_index}" -p "${num_threads}" -U "${acc}"_trim1.fastq, "${acc}"_trim2.fastq -S "${acc}".sam

        echo ">>> Sorting .sam file..."
        samtools sort -o "${acc}".sam "${acc}".sam

        echo ">>> Creating consensus sequence..."
        samtools consensus --show-del yes --show-ins no -m "simple" -aa -@ "${num_threads}" -o "${acc}".consensus.fa "${acc}".sam

        echo ">>> Removing extra files..."
        rm "${acc}_trim1.fastq" "${acc}_trim2.fastq"
        rm "${acc}.sam"
    fi

done < "$accession_txt"
