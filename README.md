
# CeleScope
CeleScope is a collection of bioinfomatics analysis pipelines developed at Singleron to process single cell sequencing data generated with Singleron products. These pipelines take paired-end FASTQ files as input and generate output files which can be used for downstream data analysis as well as a summary of QC criteria.

Detailed docs can be found in [manual](./docs/manual.md).

## Hardware/Software Requirements

- minimum 32GB RAM(to run STAR aligner)
- conda
- git

## Installation

1. Clone repo
```
git clone https://gitee.com/singleron-rd/celescope.git
# or 
git clone https://github.com/singleron-RD/CeleScope.git
```

2. Install conda packages
```
cd CeleScope
conda create -n celescope
conda activate celescope
conda install --file conda_pkgs.txt --channel conda-forge --channel bioconda --channel r --channel imperial-college-research-computing
```

3. Install celescope
```
pip install celescope
# Use pypi mirror to accelerate downloading if you are in china
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple celescope
```


## Reference genome 

### Homo sapiens

```
mkdir hs_ensembl_99
cd hs_ensembl_99

wget ftp://ftp.ensembl.org/pub/release-99/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
wget ftp://ftp.ensembl.org/pub/release-99/gtf/homo_sapiens/Homo_sapiens.GRCh38.99.gtf.gz

gunzip Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
gunzip Homo_sapiens.GRCh38.99.gtf.gz

conda activate celescope
celescope rna mkref \
 --genome_name Homo_sapiens_ensembl_99 \
 --fasta Homo_sapiens.GRCh38.dna.primary_assembly.fa \
 --gtf Homo_sapiens.GRCh38.99.gtf
```

### Mus musculus

```
mkdir mmu_ensembl_99
cd mmu_ensembl_99

wget ftp://ftp.ensembl.org/pub/release-99/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna.primary_assembly.fa.gz
wget ftp://ftp.ensembl.org/pub/release-99/gtf/mus_musculus/Mus_musculus.GRCm38.99.gtf.gz

gunzip Mus_musculus.GRCm38.dna.primary_assembly.fa.gz 
gunzip Mus_musculus.GRCm38.99.gtf.gz

conda activate celescope
celescope rna mkref \
 --genome_name Mus_musculus_ensembl_99 \
 --fasta Mus_musculus.GRCm38.dna.primary_assembly.fa \
 --gtf Mus_musculus.GRCm38.99.gtf
```

## Quick start

### Single cell RNA-Seq

1. Prepare mapfile

Mapfile is a tab-delimited text file(.tsv) containing at least three columns. Each line of mapfile represents a pair of fastq files(Read 1 and Read 2).

First column: Fastq file prefix. Fastq files must be gzipped.

Second column: Fastq directory.

Third column: Sample name, which is the prefix of all generated files. One sample can have multiple fastq files.

Fourth column: Optional, force cell number (scRNA-Seq) or match_dir (scVDJ).

Sample mapfile:
```
$cat ./my.mapfile
R2007197    /SGRNJ/DATA_PROJ/dir1	sample1
R2007199    /SGRNJ/DATA_PROJ/dir2	sample1
R2007198    /SGRNJ/DATA_PROJ/dir1   sample2

$ls /SGRNJ/DATA_PROJ/dir1
R2007198_L2_2.fq.gz
R2007198_L2_1.fq.gz
R2007197_L2_2.fq.gz
R2007197_L2_1.fq.gz

$ls /SGRNJ/DATA_PROJ/dir2
R2007199_L2_2.fq.gz
R2007199_L2_1.fq.gz
```

2. Run `multi_rna` to create shell scripts
```
conda activate celescope
multi_rna \
 --mapfile ./my.mapfile \
 --genomeDir {some path}/hs/ensembl_99 \
 --thread 8 \
 --mod shell
```

`--mapfile` Required, mapfile path.

`--genomeDir` Required, genomeDir directory.

`--thread` Maximum number of threads to use, default=4.  

`--mod` Create "sjm"(simple job manager https://github.com/StanfordBioinformatics/SJM) or "shell" scripts. 

Shell scripts will be created in `./shell` directory, one script per sample. The shell scripts contains all the steps that need to be run.

3. Run shell scripts under current directory

`sh ./shell/{sample}.sh`

### Single Cell VDJ

Running single Cell VDJ is almost the same as running single Cell RNA-Seq, except that the arguments of `multi_vdj` are somewhat different.

1. Prepare mapfile

If you have paired single cell RNA-seq and VDJ samples, the single cell RNA-Seq directory after running CeleScope is called `matched_dir`. You can write matched_dir's path as the fourth column of mapfile(optional).

```
R2007197    /SGRNJ/DATA_PROJ/dir    sample1 /SGRNJ/Projects/sample1
```

2. Run `multi_vdj` to create shell scripts

```
conda activate celescope
multi_vdj \
 --mapfile ./my.mapfile \
 --type TCR \
 --thread 8 \
 --mod shell \
```  

`--type` Required. TCR or BCR.   

3. Run shell scripts under current directory
