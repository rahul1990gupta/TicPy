import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = ['bunch==1.0.1']

setup(name='ticpy',
      version='0.0',
      description='ticpy',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='tic tac toe in python',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires
)