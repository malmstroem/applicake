from setuptools import setup

setup(
    name="base",
    version="0.0.8",
    author="Lorenz Blum",
    maintainer=['Lorenz Blum', 'Witold Wolski'],
    author_email="blum@id.ethz.ch",
    maintainer_email=["blum@id.ethz.ch",'wewolski@gmail.com'],
    description="A framework that simplifies the wrapping of external tools by standardizing input parameters, logging messages and output streams.",
    license="BSD",
    packages=['base'],
    include_package_data=True,
    url='https://github.com/base-tools',
    install_requires=[]
)