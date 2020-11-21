import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dograf", # Replace with your own username
    version="0.0.1",
    author="Dennis Ying",
    author_email="dennisyingswebpages@gmail.com",
    description="Basic Grafana Setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TwelfthGhast/doggraf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)