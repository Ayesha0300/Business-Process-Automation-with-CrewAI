from setuptools import setup, find_packages

setup(
    name='myfirstcrewaiproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # ...existing dependencies...
    ],
    entry_points={
        'console_scripts': [
            'kickoff=myfirstcrewaiproject.main:main',  # Ensure this line is correct
        ],
    },
)
