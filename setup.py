from setuptools import find_packages, setup

setup(name='energyPATHWAYS',
      version='0.1',
      description='Software package for long-term energy system modeling',
      url='https://github.com/energyPATHWAYS/energyPATHWAYS',
      author='Ben Haley, Ryan Jones, Ana Mileva',
      packages=find_packages(),
      install_requires=['pandas',
                        'numpy',
                        'scipy',
                        'pint',
                        'pyomo',
                        'datetime',
                        'pytz',
                        'profilehooks',
                        'psycopg2',
                        'matplotlib', # util.py
                        'sklearn', # dispatch_classes.py
#                        'pathos'
                        ],
      extras_require = {
        'documentation': ["Sphinx"]
      }
)
