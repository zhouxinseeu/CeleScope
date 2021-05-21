import configparser
import abc

from celescope.tools.__init__ import GENOME_CONFIG


def parse_genomeDir(genomeDir):
    config_file = f'{genomeDir}/{GENOME_CONFIG}'
    config = configparser.ConfigParser()
    config.read(config_file)
    genome = config['genome']
    return genome


class Mkref():
    def __init__(self, genome_type, args):
        self.genomeDir = args.genomeDir
        self.thread = args.thread
        self.genome_name = args.genome_name
        self.genome_type = genome_type

        # out file
        self.config_file = f'{self.genomeDir}/{GENOME_CONFIG}'
    
    @abc.abstractmethod
    def run(self):
        return

    @abc.abstractmethod
    def write_config(self):
        return


def get_opts_mkref(parser, sub_program):
    if sub_program:
        parser.add_argument("--genomeDir", default='./')
        parser.add_argument("--thread", default=6)
        parser.add_argument("--genome_name", required=True)
