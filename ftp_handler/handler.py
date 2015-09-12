__author__ = 'saurabh'
import helper
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-rootDir", default=None, help="Set Ip")
parser.add_argument("-remoteDir", default=None, help="Set Ip")
parser.add_argument("-t", default="s",  help="Single File Upload")
parser.add_argument("-f", default=None,  help="Single File Upload")
args = parser.parse_args()

if (args.rootDir ==None or args.remoteDir ==None):
    print "Root or Remote Directory Not Specified"
else:
    if args.t == "s":
        helper.upload_single_to_ftp(rootDir=args.rootDir, remoteDir=args.remoteDir, file=args.f)
    else:
        files = helper.get_files_from_local(rootDir=args.rootDir)
        helper.upload_multiple_to_ftp(rootDir=args.rootDir, remoteDir=args.remoteDir , files=files)




