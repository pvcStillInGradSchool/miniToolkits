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
  new_str = sys_argv[4]
  paths = list(root.glob('**/*.' + suffix))
  total_count = 0
  for path in paths:
    old_name = str(path)
    count = 0
    with path.open() as old_file:
      for line in old_file:
        if old_str in line:
          print(line, end='')
          count += 1
    if count > 0:
      print(str(count) + ' line(s) found in ' + old_name)
      total_count += count
  print(str(total_count) + ' line(s) found in all ' + suffix + ' file(s).')
  return total_count


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
