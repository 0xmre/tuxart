from setuptools import setup

setup(name='install',
      version='3',
      description='Tux generator for arbitrary kernel',
      url='https://github.com/HommeOursPorc/TuxArt',
      author='HommeOursPorc',
      author_email='',
      license='MIT',
      packages=['install'],
      install_requires=[
          'cairosvg',
      ],
      zip_safe=False)
