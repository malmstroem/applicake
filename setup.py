from setuptools import setup
import numpy

setup(
    name="applibase",
    version="0.0.8",
    author="Lorenz Blum",
    maintainer=['Lorenz Blum', 'Witold Wolski'],
    author_email="blum@id.ethz.ch",
    maintainer_email=["blum@id.ethz.ch",'wewolski@gmail.com'],
    description="A framework that simplifies the wrapping of external tools by standardizing input parameters, logging messages and output streams.",
    license="BSD",
    packages=['appliapps','applicake','tests'],
    include_package_data=True,
    include_dirs=[numpy.get_include()],
    url='https://github.com/applicake-tools',
    install_requires=[]
)