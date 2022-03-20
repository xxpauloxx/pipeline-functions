import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pipeline_functions",
    version="0.0.1",
    license='GPLv3+',
    author="Paulo Roberto",
    author_email="paulo.pinda@gmail.com",
    description="Class for manipulating a pipeline of functions, creating chains of functions processing the same context",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xxpauloxx/pipeline-functions",
    project_urls={
        "Bug Tracker": "https://github.com/xxpauloxx/pipeline-functions/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=("examples", "tests")),
    python_requires=">=3.6",
)
