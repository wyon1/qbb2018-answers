
grep -v "^@" ~/qbb2018-answers/rawdata/SRR072893.sam | grep -v 2110000 | datamash groupby --sort 3 count 3 > alingments_per_chromosome.sh
