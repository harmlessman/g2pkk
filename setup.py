import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

required_packages = [
            'jamo',
            'nltk',
        ]


setuptools.setup(
    name="g2pkk",
    version="0.1.2",
    author="harmlessman",
    author_email="harmlessman17@gmail.com",
    description="g2pkk: g2p module for Korean(cross platform)",
    install_requires=required_packages,
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harmlessman/g2pkk",
    packages=setuptools.find_packages(),
    package_data={'g2pkk': ['g2pkk/idioms.txt', 'g2pkk/rules.txt', 'g2pkk/table.csv']},
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
