'''
the setup.py file is used to configure the Python package for the Network Security project.
It is used by setuptools to define the package metadata, dependencies, and other configurations.
'''

from setuptools import setup, find_packages 
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    
    :param file_path: Path to the requirements file.
    :return: List of dependencies.
    """

    requirement_lst:List[str]=[]    
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e . lines
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    return requirement_lst
setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='VK',
    author_email="khushaliagrawal192@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)