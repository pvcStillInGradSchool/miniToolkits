#!/usr/bin/env python3
'''Scan all files with a given `suffix` in a given `path` recursively.
'''

import argparse
import pathlib
import sys


def scan_and_print(paths: list, suffix: str, old_word: str):
    '''Scan a word in all files with a given list of paths.
    '''
    word_count = 0
    file_count = 0
    for path in paths:
        old_name = str(path)
        word_count_in_file = 0
        with path.open() as old_file:
            for line in old_file:
                word_count_in_line = line.count(old_word)
                if word_count_in_line > 0:
                    word_count_in_file += word_count_in_line
        if word_count_in_file > 0:
            print(f'{word_count_in_file} "{old_word}"(s) found in {old_name}')
            word_count += word_count_in_file
            file_count += 1
    print(f'{word_count} "{old_word}"(s) found in {file_count} {suffix}',
        'file(s)')
    return word_count


def scan_and_delete(paths: list, old_word: str):
    '''Scan a word in all files in a given list of paths and delete the lines.
    '''
    for path in paths:
        old_name = str(path)
        new_name = old_name + '.temp'
        with path.open() as old_file:
            with open(new_name, 'w') as new_file:
                for line in old_file:
                    if old_word not in line:
                        new_file.write(line)
        pathlib.Path(new_name).replace(old_name)


def scan_and_replace(paths: list, old_word: str, new_word: str):
    '''Scan a word in all files in a given list of paths and replace the words.
    '''
    for path in paths:
        old_name = str(path)
        new_name = old_name + '.temp'
        with path.open() as old_file:
            with open(new_name, 'w') as new_file:
                for line in old_file:
                    new_file.write(line.replace(old_word, new_word))
        pathlib.Path(new_name).replace(old_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'python3 scan.py')
    parser.add_argument('-p', '--path',
        default='.', type=str,
        help='path of the folder to be scanned')
    parser.add_argument('-s', '--suffix',
        default='py', type=str,
        help='suffix (type) of files to be scanned')
    parser.add_argument('-o', '--old_word',
        default='hello', type=str,
        help='the old string to be searched')
    parser.add_argument('-n', '--new_word',
        default='world', type=str,
        help='the new string to be substituted in')
    parser.add_argument('-d', '--delete',
        action='store_true',
        help='delete the lines containing the old string')
    parser.add_argument('-r', '--replace',
        action='store_true',
        help='replace the old string with the new one')
    args = parser.parse_args()
    print(args)
    root = pathlib.Path(args.path)
    paths = list(root.glob('**/*.' + args.suffix))
    if scan_and_print(paths, args.suffix, args.old_word) > 0:
        if args.delete:
            print('Are you sure to delete these lines? [y/n]',
                end='', flush=True)
            if sys.stdin.read(1) == 'y':
                scan_and_delete(paths, args.old_word)
        elif args.replace:
            print(f'Are you sure to replace these "{args.old_word}"s',
                f'to "{args.new_word}"s? [y/n]', end='', flush=True)
            if sys.stdin.read(1) == 'y':
                scan_and_replace(paths, args.old_word, args.new_word)
