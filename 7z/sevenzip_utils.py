"""utility functions for 7-zip harness"""

import os
import shutil


def copy_from_network_drive():
    """Download 7zip from network drive"""
    source = r"\\arthas\Media\benchmarks\7ZIP\7zr_25.00.exe"
    root_dir = os.path.dirname(os.path.realpath(__file__))
    destination = os.path.join(root_dir, "7zr_25.00.exe")
    shutil.copyfile(source, destination)
