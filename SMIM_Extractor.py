'''
Created on 27.12.2016

@author: Dudenwatschn

A simple script extracting content of all numbered folders (e.g.: 00, 01, 02, ...) to a location
'''

import argparse
import subprocess
import os
import shutil
import logging

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), 
                                    os.path.join(dest, f), 
                                    ignore)
    else:
        shutil.copyfile(src, dest)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', help='Input file (.7z or extracted folder)')
    parser.add_argument('output', nargs='?', help='Where to output the folders (Creates another subfolder)')
    parser.add_argument('-z', nargs='?', help='Location to 7zip.exe', default= os.path.join(os.getenv("PROGRAMFILES", 'C:\\Program Files'), r'7-Zip\7z.exe'))
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET, format="%(module)s:[%(levelname)s] %(message)s")
    logging.log(logging.INFO,"----- Starting -----")
    args = parse_args()
    print(args.z)
    temp_path = os.path.join(os.getenv('TEMP'),"SMIM_EXTRACT")
    smim_path = None
    if '.7z' in args.input:
        logging.log(logging.INFO,"--- Extracting .7z file ---")
        smim_path = temp_path
        subprocess.call(args.z + " x -t7z \"" + args.input + "\" -o\"" + temp_path + "\" -mx=9 -y")
        logging.log(logging.INFO,"--- Finished extracting .7z file ---")
    else:
        smim_path = args.input
    out_dir = os.path.join(args.output, "Static Mesh Improvement Mod")
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    for cur_dir in os.listdir(smim_path):
        logging.log(logging.INFO,"Current Directory: " + cur_dir)
        dir_int = int
        try:
            dir_int = int(cur_dir[0:1])
        except:
            continue;
        ch_dir = os.path.join(smim_path, cur_dir)
        try:
            recursive_overwrite(ch_dir, out_dir)
        except OSError as ex:
            shutil.copy(ch_dir, out_dir)   
    logging.log(logging.INFO, "----- Finished -----")
    