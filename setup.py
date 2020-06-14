from os import path
from setuptools import setup,find_packages

exec(compile(open('gmgc_finder/gmgc_finder_version.py').read(),
             'gmgc_finder/gmgc_finder_version.py', 'exec'))


try:
    long_description = open('README.md', encoding='utf-8').read()
except:
    long_description = open('README.md').read()


setup(name='GMGC-Finder',
      version=__version__,
      description='Map genes and genome to the Global Microbial Gene Catalog (GMGC)',
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
      ],
      url='https://github.com/psj1997/GMGC_Finder',
      author='Shaojun Pan',
      author_email='shaojun1997777@gmail.com',
      license='MIT',
      packages=['gmgc_finder'],
      install_requires=[
          # Technically, numpy is not directly needed, but some downstream
          # dependencies use it and fail to declare they need it:
          'numpy',
          'Biopython',
          'scikit-bio',
          'tqdm',
          'pyyaml',
          'atomicwrites',
      ],
      package_data={
             'gmgc_finder': ['*.md']},
      zip_safe=False,
      entry_points={
            'console_scripts': ['gmgc-finder=gmgc_finder.main:main'],
      }
      )
