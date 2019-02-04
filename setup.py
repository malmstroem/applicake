from setuptools import setup, find_packages

setup(
    name="applicake",
    version="0.0.23",
    author="Andreas Quandt",
    maintainer='Lars Malmstroem',
    author_email="applicake.pypi@gmail.com",
    maintainer_email='lars@malmstroem.net',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A framework that simplifies the wrapping of external tools by standardizing input parameters, logging messages and output streams.",
    entry_points={
        'console_scripts': [
            'apl=applicake.apl:main',
        ],
    },
    license="BSD license",
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/applicake-tools/applicake',
    install_requires=[
        "configobj",
        ]
)
