from setuptools import setup, find_packages

setup(
    name='filetype_counter',
    version='0.1.0',
    description='CLI tool to count files in a folder by extension or total',
    author='Ashish Gupta',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'filecounter = filetype_counter.main:run'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)
