from setuptools import setup, find_packages

setup(
    name="microbiome-alpha",
    version="0.2.0",
    description="Diversity helpers for 16S amplicon tables",
    author="Sofia Ahmadi",
    author_email="sofia.ahmadi@example.org",
    packages=find_packages(),
    install_requires=["numpy>=1.24.0", "pandas>=2.0.0"],
)
