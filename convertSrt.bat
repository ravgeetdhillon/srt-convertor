@echo off

set filename=%1
set ext=.srt

python SRTConverter.py %filename%%ext%