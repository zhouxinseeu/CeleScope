#!/bin/env python
#coding=utf8

import argparse
import logging
from celescope.__init__ import __VERSION__, ASSAY_DICT
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description='CeleScope')
    parser.add_argument('-v', '--version', action='version', version= __VERSION__)
    subparsers = parser.add_subparsers()

    # rna
    assay = 'rna'
    text = ASSAY_DICT[assay]
    subparsers_rna = subparsers.add_parser(assay, help=text, description=text)
    subparsers_rna_sub = subparsers_rna.add_subparsers()

    from celescope.tools.sample_info import sample_info, get_opts_sample
    parser_sample = subparsers_rna_sub.add_parser('sample')
    get_opts_sample(parser_sample, True)
    parser_sample.set_defaults(func=sample_info)

    from celescope.tools.barcode import barcode, get_opts_barcode
    parser_barcode = subparsers_rna_sub.add_parser('barcode')
    get_opts_barcode(parser_barcode, True)
    parser_barcode.set_defaults(func=barcode)

    from celescope.tools.cutadapt import cutadapt, get_opts_cutadapt
    parser_cutadapt = subparsers_rna_sub.add_parser('cutadapt')
    get_opts_cutadapt(parser_cutadapt, True)
    parser_cutadapt.set_defaults(func=cutadapt)

    from celescope.tools.STAR import STAR, get_opts_STAR
    parser_STAR = subparsers_rna_sub.add_parser('STAR')
    get_opts_STAR(parser_STAR, True)
    parser_STAR.set_defaults(func=STAR)

    from celescope.tools.featureCounts import featureCounts, get_opts_featureCounts
    parser_featureCounts = subparsers_rna_sub.add_parser('featureCounts')
    get_opts_featureCounts(parser_featureCounts, True)
    parser_featureCounts.set_defaults(func=featureCounts)

    from celescope.tools.count import count, get_opts_count
    parser_count = subparsers_rna_sub.add_parser('count')
    get_opts_count(parser_count, True)
    parser_count.set_defaults(func=count)

    from celescope.tools.analysis import analysis, get_opts_analysis
    parser_analysis = subparsers_rna_sub.add_parser('analysis')
    get_opts_analysis(parser_analysis, True)
    parser_analysis.set_defaults(func=analysis) 

    from celescope.rna.run import run
    parser_run = subparsers_rna_sub.add_parser('run', help='run all steps', conflict_handler='resolve')
    get_opts_sample(parser_run, False)
    get_opts_barcode(parser_run, False)
    get_opts_cutadapt(parser_run, False)
    get_opts_STAR(parser_run, False)
    get_opts_featureCounts(parser_run, False)
    get_opts_count(parser_run, False)
    get_opts_analysis(parser_run, False)
    parser_run.set_defaults(func=run) 

    # rna_virus
    assay = 'rna_virus'
    text = ASSAY_DICT[assay]
    subparsers_rna_virus = subparsers.add_parser(assay, help=text, description=text)
    subparsers_rna_virus_sub = subparsers_rna_virus.add_subparsers()

    parser_sample = subparsers_rna_virus_sub.add_parser('sample', description='sample infomation')
    get_opts_sample(parser_sample, True)
    parser_sample.set_defaults(func=sample_info)

    from celescope.tools.barcode import barcode, get_opts_barcode
    parser_barcode = subparsers_rna_virus_sub.add_parser('barcode')
    get_opts_barcode(parser_barcode, True)
    parser_barcode.set_defaults(func=barcode)

    from celescope.tools.cutadapt import cutadapt, get_opts_cutadapt
    parser_cutadapt = subparsers_rna_virus_sub.add_parser('cutadapt')
    get_opts_cutadapt(parser_cutadapt, True)
    parser_cutadapt.set_defaults(func=cutadapt)

    from celescope.tools.STAR import STAR, get_opts_STAR
    parser_STAR = subparsers_rna_virus_sub.add_parser('STAR')
    get_opts_STAR(parser_STAR, True)
    parser_STAR.set_defaults(func=STAR)

    from celescope.rna_virus.STAR_virus import STAR_virus, get_opts_STAR_virus
    parser_STAR_virus = subparsers_rna_virus_sub.add_parser('STAR_virus')
    get_opts_STAR_virus(parser_STAR_virus, True)
    parser_STAR_virus.set_defaults(func=STAR_virus)

    from celescope.tools.featureCounts import featureCounts, get_opts_featureCounts
    parser_featureCounts = subparsers_rna_virus_sub.add_parser('featureCounts')
    get_opts_featureCounts(parser_featureCounts, True)
    parser_featureCounts.set_defaults(func=featureCounts)

    from celescope.tools.count import count, get_opts_count
    parser_count = subparsers_rna_virus_sub.add_parser('count')
    get_opts_count(parser_count, True)
    parser_count.set_defaults(func=count)

    from celescope.rna_virus.count_virus import count_virus, get_opts_count_virus
    parser_count_virus = subparsers_rna_virus_sub.add_parser('count_virus')
    get_opts_count_virus(parser_count_virus, True)
    parser_count_virus.set_defaults(func=count_virus) 

    from celescope.rna_virus.analysis_rna_virus import analysis_rna_virus, get_opts_analysis_rna_virus
    parser_analysis_rna_virus = subparsers_rna_virus_sub.add_parser('analysis_rna_virus')
    get_opts_analysis_rna_virus(parser_analysis_rna_virus, True)
    parser_analysis_rna_virus.set_defaults(func=analysis_rna_virus)

    from celescope.rna_virus.run import run
    parser_run = subparsers_rna_virus_sub.add_parser('run', help='run all steps', conflict_handler='resolve')
    get_opts_sample(parser_run, False)
    get_opts_barcode(parser_run, False)
    get_opts_cutadapt(parser_run, False)
    get_opts_STAR(parser_run, False)
    get_opts_STAR_virus(parser_run, False)
    get_opts_featureCounts(parser_run, False)
    get_opts_count_virus(parser_run, False)
    get_opts_analysis_rna_virus(parser_run, False)
    parser_run.set_defaults(func=run)    

    # capture_virus
    assay = 'capture_virus'
    text = ASSAY_DICT[assay]
    subparsers_capture_virus = subparsers.add_parser(assay, help=text, description=text)
    subparsers_capture_virus_sub = subparsers_capture_virus.add_subparsers()

    parser_sample = subparsers_capture_virus_sub.add_parser('sample')
    get_opts_sample(parser_sample, True)
    parser_sample.set_defaults(func=sample_info)

    parser_barcode = subparsers_capture_virus_sub.add_parser('barcode')
    get_opts_barcode(parser_barcode, True)
    parser_barcode.set_defaults(func=barcode)

    parser_cutadapt = subparsers_capture_virus_sub.add_parser('cutadapt')
    get_opts_cutadapt(parser_cutadapt, True)
    parser_cutadapt.set_defaults(func=cutadapt)

    parser_STAR_virus = subparsers_capture_virus_sub.add_parser('STAR_virus')
    get_opts_STAR_virus(parser_STAR_virus, True)
    parser_STAR_virus.set_defaults(func=STAR_virus)

    from celescope.capture_virus.count_capture_virus import count_capture_virus, get_opts_count_capture_virus
    parser_count_capture_virus = subparsers_capture_virus_sub.add_parser('count_capture_virus')
    get_opts_count_capture_virus(parser_count_capture_virus, True)
    parser_count_capture_virus.set_defaults(func=count_capture_virus)

    from celescope.capture_virus.run import run
    parser_run = subparsers_capture_virus_sub.add_parser('run', help='run all steps', conflict_handler='resolve')
    get_opts_sample(parser_run, False)
    get_opts_barcode(parser_run, False)
    get_opts_cutadapt(parser_run, False)
    get_opts_STAR_virus(parser_run, False)
    get_opts_count_capture_virus(parser_run, False)
    parser_run.set_defaults(func=run)

    # fusion
    assay = 'fusion'
    text = ASSAY_DICT[assay]
    subparsers_fusion = subparsers.add_parser(assay, help=text, description=text)
    subparsers_fusion_sub = subparsers_fusion.add_subparsers()

    parser_sample = subparsers_fusion_sub.add_parser('sample')
    get_opts_sample(parser_sample, True)
    parser_sample.set_defaults(func=sample_info)

    parser_barcode = subparsers_fusion_sub.add_parser('barcode')
    get_opts_barcode(parser_barcode, True)
    parser_barcode.set_defaults(func=barcode)

    parser_cutadapt = subparsers_fusion_sub.add_parser('cutadapt')
    get_opts_cutadapt(parser_cutadapt, True)
    parser_cutadapt.set_defaults(func=cutadapt)

    from celescope.fusion.STAR_fusion import STAR_fusion, get_opts_STAR_fusion
    parser_STAR_fusion = subparsers_fusion_sub.add_parser('STAR_fusion')
    get_opts_STAR_fusion(parser_STAR_fusion, True)
    parser_STAR_fusion.set_defaults(func=STAR_fusion)

    from celescope.fusion.count_fusion import count_fusion, get_opts_count_fusion
    parser_count_fusion = subparsers_fusion_sub.add_parser('count_fusion')
    get_opts_count_fusion(parser_count_fusion, True)
    parser_count_fusion.set_defaults(func=count_fusion)

    from celescope.fusion.run import run
    parser_run = subparsers_fusion_sub.add_parser('run', help='run all steps', conflict_handler='resolve')
    get_opts_sample(parser_run, False)
    get_opts_barcode(parser_run, False)
    get_opts_cutadapt(parser_run, False)
    get_opts_STAR_fusion(parser_run, False)
    get_opts_count_fusion(parser_run, False)
    parser_run.set_defaults(func=run)

    # smk
    assay = 'smk'
    text = ASSAY_DICT[assay]
    subparsers_assay = subparsers.add_parser(assay, help=text, description=text)
    subparsers_assay_sub = subparsers_assay.add_subparsers()

    parser_tmp = subparsers_assay_sub.add_parser('sample')
    get_opts_sample(parser_tmp, True)
    parser_tmp.set_defaults(func=sample_info)

    parser_tmp = subparsers_assay_sub.add_parser('barcode')
    get_opts_barcode(parser_tmp, True)
    parser_tmp.set_defaults(func=barcode)

    parser_tmp = subparsers_assay_sub.add_parser('cutadapt')
    get_opts_cutadapt(parser_tmp, True)
    parser_tmp.set_defaults(func=cutadapt)

    from celescope.smk.mapping_smk import mapping_smk, get_opts_mapping_smk
    parser_tmp = subparsers_assay_sub.add_parser('mapping_smk')
    get_opts_mapping_smk(parser_tmp, True)
    parser_tmp.set_defaults(func=mapping_smk)

    from celescope.smk.count_smk import count_smk, get_opts_count_smk
    parser_tmp = subparsers_assay_sub.add_parser('count_smk')
    get_opts_count_smk(parser_tmp, True)
    parser_tmp.set_defaults(func=count_smk)

    from celescope.smk.analysis_smk import analysis_smk, get_opts_analysis_smk
    parser_tmp = subparsers_assay_sub.add_parser('analysis_smk')
    get_opts_analysis_smk(parser_tmp, True)
    parser_tmp.set_defaults(func=analysis_smk)

    from celescope.smk.run import run
    parser_tmp = subparsers_assay_sub.add_parser('run', help='run all steps', conflict_handler='resolve')
    get_opts_sample(parser_tmp, False)
    get_opts_barcode(parser_tmp, False)
    get_opts_cutadapt(parser_tmp, False)
    get_opts_mapping_smk(parser_tmp, False)
    get_opts_count_smk(parser_tmp, False)
    get_opts_analysis_smk(parser_tmp, False)
    parser_tmp.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
