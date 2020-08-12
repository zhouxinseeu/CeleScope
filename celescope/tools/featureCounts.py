#!/bin/env python
#coding=utf8

import os, re
import logging
import subprocess
import glob
import sys
from tools.utils import format_number
from tools.utils import glob_genomeDir
from tools.report import reporter

logger1 = logging.getLogger(__name__)


def get_opts_featureCounts(parser, sub_program): 

    parser.add_argument('--gtf_type', help='Specify feature type in GTF annotation', default='exon')
    if sub_program:
        parser.add_argument('--genomeDir', required=True)
        parser.add_argument('--thread', default=1)
        parser.add_argument('--input', required=True)
        #parser.add_argument('--format', default='BAM')
        parser.add_argument('--outdir', help='output dir',required=True)
        parser.add_argument('--sample', help='sample name', required=True)


def format_stat(log, samplename):
    #Assigned, Unassigned_NoFeatures, Unassigned_Ambiguity=(0, 0, 0)
    tmp_arr = []
    fh = open(log, 'r')
    with open(os.path.dirname(log) + '/stat.txt', 'w') as stat_fh:
        p1 = re.compile(r'Assigned.*?(\d+)', flags=re.S)
        p2 = re.compile(r'Unassigned_NoFeatures.*?(\d+)', flags=re.S)
        p3 = re.compile(r'Unassigned_Ambiguity.*?(\d+)', flags=re.S)
        for line in fh:
            if line.strip()=='': continue

            m1=p1.search(line.strip())
            if m1: tmp_arr.append(int(m1.group(1)))

            m2=p2.search(line)
            if m2: tmp_arr.append(int(m2.group(1)))

            m3=p3.search(line)
            if m3: tmp_arr.append(int(m3.group(1)))

        total = sum(tmp_arr)
        tmp_arr = ['%s(%.2f%%)'%(format_number(n), (n+0.0)/total*100) for n in tmp_arr]
        for t, s in zip(['Assigned', 'Unassigned_NoFeatures', 'Unassigned_Ambiguity'], tmp_arr):
            stat_fh.write('%s: %s\n'%(t, s))
    fh.close()


def featureCounts(args):
    """
    """
    logger1.info('featureCounts ...!')

    # check
    refFlat, gtf = glob_genomeDir(args.genomeDir, logger1)

    # check dir
    if not os.path.exists(args.outdir):
        os.mkdir(args.outdir)

    # run featureCounts
    outPrefix = args.outdir + '/' + args.sample
    cmd = ['featureCounts', '-a', gtf, '-o', outPrefix, '-R', 'BAM', '-T', str(args.thread),'-t',args.gtf_type , args.input]
    logger1.info('%s' % (' '.join(cmd)))
    subprocess.check_call(cmd)
    logger1.info('featureCounts done!')

    subprocess.check_call(['which', 'samtools'])

    # sort by name:BC and umi 
    logger1.info('samtools sort ...!')
    bam_basename = os.path.basename(args.input)
    cmd = ['samtools', 'sort', '-n', '-@','3', '-o', outPrefix+'_name_sorted.bam', args.outdir + '/' + bam_basename + '.featureCounts.bam']
    logger1.info('%s'%(' '.join(cmd)))
    subprocess.check_call(cmd)
    logger1.info('samtools sort done!')

    logger1.info('generate report ...!')
    format_stat(args.outdir+'/'+args.sample+'.summary', args.sample)
    t = reporter(name='featureCounts', sample=args.sample, stat_file=args.outdir + '/stat.txt', outdir=args.outdir + '/..')
    t.get_report()
    logger1.info('generate report done!')


