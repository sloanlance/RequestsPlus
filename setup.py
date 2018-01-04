from setuptools import setup, find_packages

setup(
    name = 'requestsplus',
    version = '0.1.0',
    keywords = ('requests', ),
    description = 'RequestsPlus is a wrapper for the common Python "requests" library, with methods to make some tasks easier.',
    license = None,
    install_requires = ['requests'],
    include_package_data=True,
    zip_safe=True,

    author = 'Lance E Sloan (sloanlance)',
    author_email = 'sloanlance@gmail.com',

    url = 'https://github.com/sloanlance/RequestsPlus',

    packages = find_packages(),
    platforms = 'any',
)