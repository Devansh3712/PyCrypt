from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = '''Encryption and Decryption tool made using python'''
  
setup( 
        name ='pycrypt', 
        version ='1.0', 
        author ='Devansh Singh', 
        author_email ='devanshamity@gmail.com', 
        url ='https://github.com/Devansh3712/pycrypt', 
        description ='Cryption tool', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(),
        entry_points ={ 
            'console_scripts': [ 
                'pycrypt = pycrypt.pycrypt:main'
            ] 
        }, 
        classifiers =[
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ],
        install_requires = requirements, 
        zip_safe = False
) 