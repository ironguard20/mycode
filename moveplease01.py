#!/usr/bin/env python3
# import modules
import shutil
import os

# set working directory
os.chdir('/home/student/mycode/')

# move raynor to ceph storage
shutil.move('raynor.obj', 'ceph_storage/')

# set a new name for kerrigan.obj
xname = input('What is the new name for kerrigan.obj? ')

# move kerrigan.obj with a new name to ceph_storage
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
