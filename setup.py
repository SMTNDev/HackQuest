from setuptools import setup, find_packages

setup(
    name="hackquest",  # PyPI name of the package
    version="1.0.0",
    description="A terminal-based hacking simulator game",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="SMTNDev",
    author_email="smtndeveloper@gmail.com",
    url="https://github.com/SMTNDev/HackQuest",
    packages=find_packages(),
    install_requires=[
        "colorama==0.4.6",
        "termcolor==2.3.0",
        "pyfiglet==0.8.post1",
        "rich==13.5.2",
        "blessings==1.7",
        "cryptography==39.0.0",
        "curses-2048==0.2.0",
    ],
    entry_points={
        "console_scripts": [
            "hackquest=hackquest.main:main",  # Command-line entry point
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    include_package_data=True,  # Include non-code files (e.g., README.md)
)
