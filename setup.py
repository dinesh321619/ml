from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]
    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    author="dinesh",
    author_email="dineshkarthikdineshkarthik40@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
