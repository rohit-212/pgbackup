from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
        name='pgbackup',
        version='0.1.0',
        author='Rohit Surve',
        author_email='rohits1892@gmail.com',
        description='A utility key for backing up PostgreSQL databases.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/rohit-212/pgbackup',
        packages=find_packages('src'),
        package_dir={'':'src'},
        install_requires=['boto3'],
        python_requires='>=3.6',
        entry_points={
            'console_scripts': [
                'pgbackup=pgbackup.cli:main'
                ],
            }
        )
