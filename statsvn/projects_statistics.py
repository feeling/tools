__author__ = 'hill'

import os
import subprocess
import platform
import getopt
import sys
import datetime

def usage():
    print "cmd  --begin=yyyy-MM-dd --end=yyyy-MM-dd"

def main(argv):
    ymd='%Y-%m-%d'
    now = datetime.datetime.now()
    _begin = (now + datetime.timedelta(days =-9)).strftime(ymd)
    _end = now.strftime(ymd)

    try:
        opts, args = getopt.getopt(argv, "h:", ["help", "begin=", "end="])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()                     
            sys.exit()                  
        elif opt in ("--begin"):
            _begin = arg
        elif opt in ("--end"):
            _end = arg
    print "duration begin:%s - end:%s:" % (_begin, _end)
    cur_dir = os.path.split(os.path.realpath(__file__))[0]
    file_object = open('projects.txt')
    for line in file_object:
        if not line.strip():
            continue
        print line
        line = line.strip()
        branch = line.split(os.sep)[-1]
        print branch
        sysstr = platform.system()
        if(sysstr =="Windows"):
            print ("Call Windows tasks")
            doWinJobs(cur_dir,line, branch,_begin, _end)
        elif(sysstr == "Linux"):
            print ("Call Linux tasks")
            doLinuxJobs(cur_dir,line, branch)
        else:
            print ("Other System tasks")
            doMacJobs(cur_dir,line, branch)

def execute(command):
    process_result = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        buff = process_result.stdout.readline()
        if buff.strip():
            print buff
        if buff == '' and process_result.poll() != None:
            break

def doMacJobs(cur_dir, strPath, strBranch, begin, end):
    execute("cd %s" % strPath)
    

def doLinuxJobs(cur_dir, strPath, strBranch, begin, end):
    execute("cd %s" % strPath)
    

def doWinJobs(cur_dir, strPath, strBranch, begin, end):
    execute("cd %s" % strPath)
    execute("svn up")
    log_cmd = "svn log -r{%s}:{%s} -v --xml %s > %s\svn.log" % (begin, end, strPath, strPath)
    print "execute command :%s" % log_cmd
    execute(log_cmd)
    execute("cd %s" % cur_dir)
    execute("mkdir %s" % strBranch)
    execute("java -jar statsvn.jar %s\svn.log %s -output-dir %s\%s -xml -include **/*.java:**/*.jsp:**/*.js:**/*.css:**/*.xml" % (strPath, strPath,cur_dir, strBranch))


if __name__ == '__main__':
    main(sys.argv[1:])
