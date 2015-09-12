__author__ = 'saurabh'
import os
import ftplib
server = '182.50.132.19'
username = 'spandey2405'
password = "Siddyking123"

def get_files_from_local(rootDir):
    os.chdir(rootDir)
    files = []
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        if dirName == "/home/saurabh/w/web/api":
            for fname in fileList:
                files.append(fname)
    return files

def upload_multiple_to_ftp(rootDir, remoteDir ,files):
    ftp = ftplib.FTP(server, username, password)
    os.chdir(rootDir)
    ftp.cwd(remoteDir)
    for file in files:
        myfile = open(file, 'r')
        ftp.storlines('STOR ' + file, myfile)


def upload_single_to_ftp(rootDir, remoteDir ,file):
    ftp = ftplib.FTP(server, username, password)
    os.chdir(rootDir)
    ftp.cwd(remoteDir)
    myfile = open(file, 'r')
    ftp.storlines('STOR ' + file, myfile)

