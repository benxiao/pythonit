from setuptools import setup

setup(
    name='chemist',
    version='0.1.0',
    py_modules = ['chemist'],
    install_requires=[],
    entry_points = '''
        [console_scripts]
        chemist=main:main
    '''
)