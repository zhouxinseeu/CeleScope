# Change Log

## [unreleased] - 2021-06-09
### Added
### Changed
### Fixed
### Removed

## [1.3.1] - 2021-06-09
### Added

- Add wdl workflow.

- Add Seurat hashtag method in `celescope tag count_tag`. To get Seurat hashtag output, use `--debug`. However, there was a unsolved problem with this method: https://github.com/satijalab/seurat/issues/2549.

### Changed

- `{sample}_UMI_count_filtered1.tsv` in mapping_vdj changed to `{sample}_UMI_count_filtered.tsv` (remove `1` after filtered)

### Fixed and Removed

- Remove h5 file generation in R to avoid memory issues.


## [1.3.0] - 2021-05-28
 
### Added

- `mkref` subcommand. See `celescope rna mkref`, `celescope fusion mkref` and `celescope virus mkref` for details.

### Changed

- Change the way to handle duplicate gene_name and gene_id in gtf file.

Previous:

    - one gene_name with multiple gene_id: "_{count}" will be added to gene_name.
    - one gene_id with multiple gene_name: newer gene_name will overwrite older gene_name.
    - duplicated (gene_name, gene_id): "_{count}" will be added to gene_name.

Now:

    - one gene_name with multiple gene_id: "_{count}" will be added to gene_name.
    - one gene_id with multiple gene_name: error.
    - duplicated (gene_name, gene_id): ignore duplicated records and print a warning.

### Fixed

- Fix `count tag` metrics order in merge.xls

### Removed

- Remove `--fusion_pos` from `celescope.fusion.count_fusion`

 
## [1.2.0] - 2021-05-19
 
### Added

- Assay `rna` outputs .h5 file in 06.analysis directory.

### Changed

- Update Seurat from 2.3.4 to 4.0.1.

- `--genomeDir` in `celescope.fusion.star_fusion` changed to `--fusion_genomeDir` to avoid misunderstanding.

- Step `star` sort bam by samtools instead of STAR to avoid potential `not enough memory for BAM sorting` error: https://github.com/alexdobin/STAR/issues/1136

### Removed

- Assay `rna` no longer outputs tab-delimited expression matrix file in 05.count directory.

 
## [1.1.9] - 2021-04-25
 
### Added

- Add parameter `--coefficient`  to `celescope tag count_tag` and `multi_tag`
    
    Default `0.1`. Minimum signal-to-noise ratio is calulated as `SNR_min = max(median(SNRs) * coefficient, 2)`

- Add `.metrics.json`

- Add `scopeV1` chemistry support.
 
### Changed
  
- Optimize speed and memory usage of step `barcode`(~2X faster) and `celescope.tools.count.downsample`(~15-25X faster, 1/2 memory usage).

- Change filtering of linker from allowing two mismatches in total to two mismatches per segment; this will slightly increase the valid reads percentage.

- Default output fastq files of `barcode` and `cutadapt` are not gzipped. Use `--gzipped` to get gzipped output.

- Change the display of Barcode-rank plot in html report. 

### Fixed

- Fix a bug that `celescope.tools.barcode.mismatch` cannot output all sequences correctly when n_mismatch>=2.

- Fix an error when Numpy >= 1.2.0.

- VDJ merge.xls can display all the metrics correctly.

### Removed

- Remove fastqc from `barcode` step.

 
## [1.1.8] - 2021-03-26
 
### Added

- Add read consensus to VDJ pipeline. 

    A consensus step was added before mapping to merge all the reads of the same
    (barcode, UMI) into one UMI. For defailed consensus algorithm, refer to `celescope.tools.consensus`.  
    multi_vdj adds the parameter `--not_consensus` that you can skip the consensus step, and get the same results as v1.1.7.   

- Add parameter `--species` to `celescope vdj mapping_vdj` and `multi_vdj`.

    `--species` can be one of:
    - `hs`: human
    - `mmu`: mouse

- Add parameter `--cell_calling_method` to `celescope rna count` and `multi_rna`.

    `--cell_calling_method` can be one of:  
    - `auto`: Same result as v1.1.7.  
    - `cellranger3`: Refer to the cell_calling algorithm of cellranger3, and the result is similar to cellranger3.  
    - `reflection`: Use the inflection point of the barcode-rank curve as the UMI threshold. The minimum UMI value is changed from initial threshold / 10 to initial threshold / 2 to prevent the use of a lower inflection point when there are multiple inflection points.  

- Add 4 tags to featureCounts bam.

    - `CB`: cell barcode
    - `UB`: UMI
    - `GN`: gene name
    - `GX`: gene id

- Add `--STAR_param` to `celescope rna STAR`

    Additional parameters of STAR can be passed into the `STAR` step.

### Changed

- One sample can have different chemistry fastq in mapfile.  Version <= v1.1.7 will report this as an error.

- Gtf file can be gzipped.

- `multi_rna` can use 3 paramters: `--STAR_index`, `--gtf` and `--refFlat` instead of `--genomeDir` 

- Step `snpCalling` use mutract.


## [1.1.7] - 2020-12-16

### Added

- Automatically detect Singleron chemistry version.

### Changed

- FeatureCounts use strand specificity.

- Cutadapt default `overlap` change from `5` to `10`.

- VDJ sort `NA` last.

- `match clonetypes` are sorted by barcode_count(Frequency) first, then clonetype_ID.




