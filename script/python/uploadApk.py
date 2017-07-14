#!/usr/bin/python
# -*- coding: utf-8 -*-
from ftplib import FTP_TLS
import os.path
import sys
from tqdm import tqdm
import getopt
from os import listdir

session = FTP_TLS()


# session.set_debuglevel(1);


def connectLoginHuatianServer():
    session.connect('61.135.251.56', "16321");
    session.auth()
    session.prot_p()
    session.login('gzlichangjie', '-k)T$G$w1!');
    print "login success..."


def cdToDestination():
    directory = "/3g/client/huatian/"
    session.cwd(directory);


def getBackupName(oldVersion, newVersion):
    return oldVersion + "to" + newVersion;


def backupHuatianApk(oldVersion, newVersion, fileName):
    print "start backup "+oldVersion
    session.mkd("./BACKUP/" + getBackupName(oldVersion, newVersion))
    session.rename("./" + fileName, "./BACKUP/" + getBackupName(oldVersion, newVersion) + "/" + fileName)
    print "backup finish"


class HuatianUpload:
    fileProgress = 0;
    totalSize = 0;

    def __init__(self, totalSize):
        self.totalSize = totalSize;
        self.pb = tqdm(total=100);
        self.pb.update(0);
        self.prevous = 0;

    def uploadProgressCallback(self, block):
        self.fileProgress += 1024  # this line fail because sizeWritten is not initialized.
        percentComplete = self.fileProgress * 100 / self.totalSize
        self.pb.update(percentComplete - self.prevous)
        self.prevous = percentComplete;


def uploadHuatianApk(fileName):
    baseDir = 'D:\\duanlian_test\\'
    absPath = baseDir + fileName;
    totalSize = os.path.getsize(absPath);
    print "start upload " + fileName + "...";
    upload = HuatianUpload(totalSize)
    session.storbinary("STOR " + fileName, open(absPath, 'rb'), 1024, upload.uploadProgressCallback);
    print "upload " + fileName + " finished";

def uploadHuatianSpecialApk(fileName):
    directory = "/3g/client/"
    session.cwd(directory);
    uploadHuatianApk(fileName)

def usage():
    print "--oldVersion=4.4.0" \
          "--newVersion=4.5.0"

def getAllFileName(path):
        print "file name: "+str(listdir(path));

def main(argv):
    oldVersion = "0.0.0"
    newVersion = "0.0.0"
    try:
        opts, args = getopt.getopt(argv[1:], 'hv',
                                   ['oldVersion=', 'newVersion='])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit(1)
        elif o in ('--oldVersion'):
            oldVersion=a
        elif o in ('--newVersion'):
            newVersion=a

    connectLoginHuatianServer()
    cdToDestination()
    allFileNames=['huatian-bobo_huatian.apk', 'huatian-fensitong1_huatian.apk', 'huatian-fensitong_huatian.apk', 'huatian-jingyan.apk', 'huatian-nsll_huatian.apk', 'huatian-qq_huatian.apk', 'huatian-zhidao_huatian.apk', 'huatian_fensitongb_huatian.apk', 'huatian_fensitongc_huatian.apk', 'Huatian_fuyi1_huatian.apk', 'Huatian_fuyi_huatian.apk', 'huatian_huodong1_huatian.apk', 'huatian_huodong2_huatian.apk', 'huatian_huodong3_huatian.apk', 'Huatian_huodong_huatian.apk', 'Huatian_ppzuche_huatian.apk', 'Huatian_stopbb.apk', 'Huatian_zaker_huatian.apk', 'netease_huatian_android.apk']
    print  "start backup apk...\n"
    for fileName in allFileNames:
        backupHuatianApk(oldVersion,newVersion,fileName)
    print  "finish backup apk\n"

    print  "start upload apk...\n"
    for fileName in allFileNames:
        uploadHuatianApk(fileName)
    print  "finish upload apk\n"

    specialFileName="netease_huatian_android.apk";
    uploadHuatianSpecialApk(specialFileName)
if __name__ == '__main__':
    main(sys.argv)
    # baseDir = 'D:\\duanlian_test\\'
    # getAllFileName(baseDir)