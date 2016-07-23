#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
rename_dict = {'Nidoran♀': 'Nidoranf', 'Nidoran♂': 'Nidoranm', 'Farfetch&#039;d': 'Farfetch', 'Mr. Mime': 'MrMime'}
filename = sys.argv[1]
f = open(filename, 'r')
download_name = f.read()
download_name = download_name.replace("\n", "")
if rename_dict.has_key(download_name):
  print rename_dict[download_name]
else:
  print download_name
