#!/usr/bin/env python3
'''Scan and Replace.

Scan all files with a given `suffix` in a given `path` recursively, then
Replace each `old` with `new`.
'''

import pathlib
import sys


def scan_and_print(sys_argv):
  root = pathlib.Path(sys_argv[1])
  suffix = sys_argv[2]
  old_str = sys_argv[3]
  paths = list(root.glob('**/*.' + suffix))
  word_count = 0
  file_count = 0
  for path in paths:
    old_name = str(path)
    word_count_in_file = 0
    with path.open() as old_file:
      for line in old_file:
        word_count_in_line = line.count(old_str)
        if word_count_in_line > 0:
          word_count_in_file += word_count_in_line
          # print(line, end='')
    if word_count_in_file > 0:
      print('{0} "{1}"(s) found in {2}'.format(word_count_in_file, old_str, old_name))
      word_count += word_count_in_file
      file_count += 1
  print('{0} "{1}"(s) found in {2} {3} file(s)'.format(word_count, old_str, file_count, suffix))
  return word_count


def scan_and_replace(sys_argv):
  root = pathlib.Path(sys_argv[1])
  suffix = sys_argv[2]
  old_str = sys_argv[3]
  new_str = sys_argv[4]
  paths = list(root.glob('**/*.' + suffix))
  for path in paths:
    old_name = str(path)
    new_name = old_name + '.temp'
    with path.open() as old_file:
      with open(new_name, 'w') as new_file:
        for line in old_file:
          new_file.write(line.replace(old_str, new_str))
    pathlib.Path(new_name).replace(old_name)


if __name__ == '__main__':
  if (len(sys.argv) != 5):
    print('Usage:')
    print('  python3 scan_and_replace.py [root] [suffix] [old] [new]')
  else:
    if scan_and_print(sys.argv) > 0:
      print('Are you sure to replace these "{0}"s to "{1}"s? [y/n]'.format(
          sys.argv[3], sys.argv[4]), end='', flush=True)
      if (sys.stdin.read(1) == 'y'):
        scan_and_replace(sys.argv)
