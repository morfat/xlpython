from distutils.core import setup
setup(
  name = 'xlpython',
  version = '0.1',
  description = 'A small and simple class for processing excel files in python',
  author = 'Morfat Mosoti Ogega',
  author_email = 'morfatmosoti@gmail.com',
  url = 'https://github.com/morfat/xlpython', # use the URL to the github repo
  keywords = ['processing', 'python', 'excel'], # arbitrary keywords
  install_requires=['xlrd'],
  py_modules=['xlpython'],
  packages='xlpython',
)

