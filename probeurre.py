#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of Probeurre-cloner
"""
from argparse import ArgumentParser
from git import Repo
from tqdm import tqdm
import os
import sys

print(sys.argv[1:])

# Argument parsing
parser = ArgumentParser(
    description="shows statistics about comments on git repositories.")
parser.add_argument("-v", "--verbose", help="be verbose", action="store_true")
parser.add_argument("-r", "--repo", help="treat these repositories", nargs="+")
parser.add_argument("-o", "--org", help="treat repositories of these GitHub organizations", nargs="+")
parser.add_argument("-l", "--limit", help="treat at most that number of repositories per organization")
parser.add_argument("-w", "--workdir", help="directory to download files into")
args = parser.parse_args()

relativeWorkingDir = args.workdir
workingDir = os.path.join('/probeurre-data', relativeWorkingDir)
repos = args.repo

if not repos:
    parser.print_help()
    exit(1)

for repoUrl in repos:
    print('Cloning repo %s' % repoUrl)
    Repo.clone_from(repoUrl, os.path.join(workingDir, 'repo'))

print('Cloning successful')