import glob
import os

__STEPS__ = ['sample', 'barcode', 'convert', 'assemble']
__ASSAY__ = 'vdj_full_len'

soft_version = ['3.0.2', '3.1.0', '4.0.0', '6.0.0']
default_version = '4.0.0'
species_choice = ['hs', 'mmu']
soft_dict = {}
ref_dict = {}

def isDir(path_list):
    for path in path_list:
        if os.path.isdir(path):
            return path

for version in soft_version:
    soft_dict[version] = f'/SGRNJ/Database/script/soft/cellranger/cellranger-{version}/cellranger'
    ref_dict[version] = {}
    for species in species_choice:

        default_ref = glob.glob(
            f'/SGRNJ/Database/script/soft/cellranger/vdj_ref/{default_version}/{species}/refdata*')
        default_ref = isDir(default_ref)

        ref_path = glob.glob(f'/SGRNJ/Database/script/soft/cellranger/vdj_ref/{version}/{species}/refdata*')
        ref_path = isDir(ref_path)
        
        if ref_path:
            ref_dict[version][species] = ref_path
        else:
            ref_dict[version][species] = default_ref


