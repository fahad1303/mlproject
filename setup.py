from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:  str)-> List[str]:
    # This functoin will return the list of requiremnts
    requirements = []
    with open(file_path) as file_obj:
        requirements  = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        
    return requirements

setup(
name = 'ML Project',
version= '0.0.1',
author= 'fahad',
author_email='mfahadmdgr@gmail.com',
packages= find_packages(),
intall_requires= get_requirements('requirements.txt')
)