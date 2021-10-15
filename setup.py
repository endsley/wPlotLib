#from distutils.core import setup
from setuptools import setup

# read the contents of your README file
#import os
#from os import path
#this_directory = path.abspath(path.dirname(__file__))
#with open(path.join(this_directory, 'README'), encoding='utf-8') as f: 
#	long_description = f.read()

#def read_file(filename):
#	with open(os.path.join(os.path.dirname(__file__), filename)) as file:
#		return file.read()



setup(
  name = 'wplotlib',         # How you named your package folder (MyLib)
  packages = ['wplotlib'],   # Chose the same as "name"
  version = '0.39',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library that simplifies some basic plotting.',   # Give a short description about your library
  long_description='https://github.com/endsley/wPlotLib',
  #long_description=read_file('README.md'),
  long_description_content_type='text/markdown',  
  author = 'Chieh Wu',                   # Type in your name
  author_email = 'chieh.t.wu@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/endsley/wPlotLib.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/endsley/wPlotLib/archive/refs/tags/0.39.tar.gz',    # I explain this later on
  keywords = ['plot', 'data'],   # Keywords that define your package best
  include_package_data=False,
  install_requires=[            # I get to this in a second
          'matplotlib',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
