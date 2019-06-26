from setuptools import setup, find_packages

with open("README.md", "r") as ld:
    long_description = ld.read()

setup(name='tuxart',
      version='3',
      description='Tux generator for arbitrary kernel',
      url='https://github.com/HommeOursPorc/tuxart',
      author='Khaled Arsalane, Eliot Marie, Pierre Pouteau, Richard Faraji-Huon, Zakariae Boukhchen',
      author_email='khaled.arsalane@etudiant.univ-rennes1.fr',
      license='MIT',
      scripts=['bin/tuxart'],
      packages=['sources'],
      package_dir={'sources':'tuxart/sources'},
      package_data={'sources':['sprays/*.svg']},
      install_requires=[
          'kconfiglib','cairosvg',
      ],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
      ])
