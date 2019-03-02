from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="another_cms_on_s3",
    version="0.0.1",
    author="Rewati Raman",
    author_email="rewati.raman@gmail.com",
    description="This is another static site serving app, Content is stored in a s3 bucket. It can be run as stand alone server as well as can be launched as aws lambda.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/your_package/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)
