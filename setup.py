from setuptools import setup, find_packages

setup(
    name="ClassHoster",                      
    version="0.1.2",                        
    description="Host ANY Class", 
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    author="Conner Sommerfield",             
    author_email="conner.sommerfield@gmail.com",  
    url="https://github.com/RepoFactory/ClassHoster",  
    packages=find_packages(where="src"), 
    package_dir={"": "src"},
    include_package_data=True,              
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'launch = classhoster.launch:main',      
            'host = classhoster.public.hostclass:main',
            'hostall = classhoster.public.hostall:main'
        ],
    },
    python_requires=">=3.8",
)
