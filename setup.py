from setuptools import find_packages, setup

setup(
    name='TracSubversionLocation',
    version='1.0.1',
    author='Erik Rose',
    author_email='ErikRose@psu.edu',
    url='http://trac-hacks.org/wiki/SubversionLocationPlugin',
    description='Provide links to the actual URLs of Subversion-dwelling items',
    license='GPL',
    keywords='trac plugin svn subversion',
    packages=find_packages(exclude=['*.tests*']),
    install_requires=[],
    entry_points = """
    [trac.plugins]
    subversionlocation = subversionlocation
    """,
    )
