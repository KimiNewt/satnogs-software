from setuptools import setup, find_packages

setup(
    name='satlocator',
    version='0.1',
    packages=find_packages('.'),
    url='https://github.com/satnogs/satnogs-software',
    license='Mozilla',
    requires=['requests', 'bottle', 'pyephem', 'sqlite3'],
    entry_points={'console_scripts': [
        'tracker_admin_api = satlocator.tracker_admin_api:main',
        'tracker_worker_api = satlocator.tracker_worker_api:main'
    ]
    }
)
