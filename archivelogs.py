#!/usr/bin/env python

import subprocess,os,sys

def find_files():
    while 1:
        days = raw_input('\nthe number of days for archiving the logs (number): ')
        if days == 'q' or days == 'quit':
            sys.exit(0)
        logs = os.popen('find . -type f -mtime +%s -maxdepth 1' % days)
        logs_files = logs.read().split('\n')[:-1]
        if not logs_files:
            print"\nno files found!\n"
            continue
        else:
            break
    return logs_files

def check_files(n):
    for line in n:
        print line
    result = raw_input('\ngzip them or choose the duration again (yes/no/quit): ')
    return result.strip().lower()

def achive(n):
    for line in n:
        subprocess.call('gzip %s' % line,shell=True)

def move():
    backupDir = raw_input('\nmove *.gz to /home/backup or you specify the directory: ')
    if backupDir == 'q' or backupDir == 'quit'
        sys.exit(0)
    if not os.path.exists(backupDir):
        subprocess.call('mkdir %s' % backupDir,shell=True)
    os.system('mv ./*.gz %s' % backupDir)

if __name__ == "__main__":
    while 1:
        files = find_files()
        answer = check_files(files)
        if answer == 'y' or answer == 'yes':
            achive(files)
            move()
            break
        elif answer == 'n' or answer == 'no':
            continue
        elif answer == 'q' or answer == 'quit':
            sys.exit(0)
