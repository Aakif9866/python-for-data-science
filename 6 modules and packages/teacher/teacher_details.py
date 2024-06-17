import os, sys
from os.path import dirname, join, abspath
parent_dir_path = abspath(join(dirname(__file__), '..'))
sys.path.insert(0, parent_dir_path)
from student import student_details


def teacher():
    print("This is teacher details")

student_details.student()
# this results in an error due to hierarchy of python
# to fix this you can use os and sys 

