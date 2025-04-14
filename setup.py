from setuptools import setup, find_packages

setup(
    name="BiblioSOM",
    version="0.1",
    author="Ihan de Oliveira Nunes",
    author_email="ihann664@gmail.com",
    description="Simplified apllication of SOM(self-organizing-map)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ApplicationSOM/BiblioSOM",
    packages=find_packages(),
    install_requires=[
        # Dependências da biblioteca, exemplo:
        "numpy>=1.19.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
