from setuptools import setup, find_packages

setup(
    name="applicake",
    version="0.0.20",
    author="Lorenz Blum",
    maintainer=['Lorenz Blum', 'Witold Wolski','Lars Malmstroem'],
    author_email="blum@id.ethz.ch",
    maintainer_email=["blum@id.ethz.ch",'wewolski@gmail.com','lars@malmstroem.net'],
    description="A framework that simplifies the wrapping of external tools by standardizing input parameters, logging messages and output streams.",
    entry_points={
        'console_scripts': [
            'apl=applicake.apl:main',
        ],
    },
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/applicake-tools/applicake',
    install_requires=[]
)
