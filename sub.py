import shlex, subprocess
from subprocess import call


print 'Enter repository address :' #http address that we copy from bitbucket url after creating repo
repo = raw_input()
call("hg clone "+repo, shell=True)


#only one file can be copied now
print 'Enter filenames to copy :'
fnames = raw_input()

print'Enter reponame'
reponame = raw_input()


print 'copying to repository'
call(["cp",fnames,reponame])

#call("hg add", shell=True)
print'adding'
subprocess.Popen(["hg", "add"],cwd="/home/jinesh/testing")

print'Enter Username of bitbucket'
username = raw_input()
print'Enter a  passphrase'
passphrase = raw_input()

print 'committing added files'
subprocess.Popen(["hg","commit","-u",username,"-Am",passphrase],cwd="/home/jinesh/testing")

print'Pushing files to repository'
subprocess.Popen(["hg", "push"], cwd="/home/jinesh/testing")
