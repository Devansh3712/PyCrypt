from setuptools import *
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
  
setup( 
        name ='pycrypt-cli',
        version = '0.5',
        author ='Devansh Singh', 
        author_email ='devanshamity@gmail.com', 
        url ='https://github.com/Devansh3712/pycrypt-cli', 
        description ='Cryption tool', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT',
        packages = ["pycryptcli"],
        include_package_data = True,
        entry_points = {
        	"console_scripts": [
        		"pycrypt=pycryptcli.__main__:pycrypt",
        	]
        },
        classifiers =[
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ],
        install_requires = requirements,
) 
