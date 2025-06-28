from setuptools import setup, find_packages

setup(
    name="openaiWrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["openai"],
    description="Decorator for creating OpenAI function tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="David",
    author_email="david@example.com",
    url="https://github.com/david/openai-wrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)