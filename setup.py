from setuptools import setup, find_packages

with open("requirements.txt") as req:
    install_requires = req.read()

setup(
    name='jazz',
    version='0.0.1',
    description='',
    url='https://github.com/madeiramadeirabr/jazz.git',
    author='SRE Team',
    author_email='sre-team@madeiramadeira.com.br',
    packages=find_packages(),
    zip_safe=False
),
