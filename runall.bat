@echo off
setlocal enabledelayedexpansion

echo Running Ycruncher...
python ycruncher\ycruncher.py
echo.

echo Running Flac...
python flac\flac.py
echo.

echo Running Blender Benchmark 4.3.0 GPU...
python blenderbenchmark\blender.py -s all -d gpu -v 4.3.0
echo.

echo Running Handbrake AV1_NVENC...
python handbrake\handbrake.py -e av1_nvenc
echo.

echo All scripts completed.
pause