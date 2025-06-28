from setuptools import setup, find_packages

setup(
    name="openaiWrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["openai"],
    description="Decorator for creating OpenAI function tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="David Lerner",
    author_email="mr.david.lerner@gmail.com",
    url="https://github.com/pilot4u/openaiWrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Commons Clause",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)