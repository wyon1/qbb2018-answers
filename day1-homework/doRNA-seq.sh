#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf


for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
   mkdir $SAMPLE
   fastqc $SAMPLE.fastq
   hisat2 -p 8 -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam 
   samtools view -S -b $SAMPLE.sam > $SAMPLE.bam
   samtools sort $SAMPLE.bam -o $SAMPLE.sorted.bam
   samtools index $SAMPLE.sorted.bam
   stringtie $SAMPLE.sorted.bam -p 8 -e -G $ANNOTATION -o $SAMPLE.gtf -B
done

