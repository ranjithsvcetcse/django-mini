import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mini_ide-Ranjith_Kumar", 
    version="0.0.1",
    author="Ranjith Kumar",
    author_email="ranjithsvcetcseb@gmail.com",
    description="A small UI editor for django apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ranjithsvcetcse/mini-project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: None"# OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)