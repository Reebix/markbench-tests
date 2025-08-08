"""Utility functions for Cinebench 2024 test script"""
import os
import re
import shutil

SCORE_PATTERN = re.compile(r"^CB (\d+\.\d+) \(.+\)$")

def get_score(output: str) -> str | None:
    """Finds score pattern from output string"""
    for line in reversed(output.splitlines()):
        match = SCORE_PATTERN.search(line)
        if match:
            return match.group(1)

    return None


def friendly_test_name(test: str) -> str:
    """Return a friendlier string given a test argument"""
    if test == "g_CinebenchCpu1Test=true":
        return "Cinebench 2023 Single Core"
    if test == "g_CinebenchCpuXTest=true":
        return "Cinebench 2023 Multicore"
    return test


def copy_from_network_drive():
    """Download 7zip from network drive"""
    source = r"\\arthas\Media\benchmarks\CinebenchR23.zip"
    root_dir = os.path.dirname(os.path.realpath(__file__))
    destination = os.path.join(root_dir, "CinebenchR23.zip")
    shutil.copyfile(source, destination)
