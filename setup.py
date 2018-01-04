from setuptools import setup, find_packages

setup(
    # Temporary name change because "requestsplus" already taken by cchen/phantomkidding!
    # I like packages in the PHP world.  On Packagist, they're named as "author_name/package_name".
    name = 'sloanlance_requestsplus',
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