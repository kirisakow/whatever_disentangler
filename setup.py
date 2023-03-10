from setuptools import find_packages, setup

setup(
    name='whatever_detangler',
    version='0.0.1',
    url='https://github.com/hail-is/hail.git',
    author='Hail Team',
    author_email='hail@broadinstitute.org',
    description='Utils for building services',
    package_data={"whatever_detangler": ["py.typed"]},
    packages=find_packages(),
    include_package_data=True,
)