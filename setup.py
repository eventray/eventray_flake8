from distutils.core import setup
from setuptools import find_packages


setup(
    name='eventray_flake8',
    version='0.0.1',
    description='Eventray flake8 plugins',
    author='Joe Lombrozo',
    author_email='joe@djeebus.net',
    url='https://eventray.com/',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'flake8_import_order.styles': [
            'eventray = eventray_flake8:EventRayStyle',
        ],
    },
)
