import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="solaxcloud",
    version="0.1.0",
    author="Frank van der Heide",
    author_email="frankvanderheide89@gmail.com",
    description="API wrapper for solax cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frank8the9tank/SolaxCloud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
