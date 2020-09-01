import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="httpower-trezar001", # Replace with your own username
    version="0.0.1",
    author="Tre Zareck",
    author_email="trezar001@gmail.com",
    description="A python tool for creating and sending HTTP requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trezar001/httpower",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
