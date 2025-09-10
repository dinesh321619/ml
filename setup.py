from setuptools import find_packages, setup

def get_requirements(filename="requirements.txt"):
    with open(filename) as f:
        requirements = f.read().splitlines()
        # Remove "-e ." if present (common in ML projects)
        requirements = [req for req in requirements if req.strip() != "-e ."]
    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A machine learning project",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.8",
)
