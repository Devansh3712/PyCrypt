from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
  
setup( 
        name ='pycrypt-cli',
        author ='Devansh Singh', 
        author_email ='devanshamity@gmail.com', 
        url ='https://github.com/Devansh3712/pycrypt', 
        description ='Cryption tool', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(),
        classifiers =[
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ],
        install_requires = requirements, 
        zip_safe = False
) 