from distutils.core import setup
import os


def get_packages(package):
    """
    Return root package & all sub-packages.
    """
    return [
        dirpath for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, '__init__.py'))
    ]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend(
            [os.path.join(base, filename) for filename in filenames])
    return {package: filepaths}


setup(
    name='avatar-gen',
    version='0.5.2.dev0',
    packages=get_packages('avatar-gen'),
    package_data=get_package_data('avatar-gen'),
    description='Using pillow for generate avatars, first letter of string in Chinese and English or random pixle like avatars.',
    author='Chen Jian',
    author_email='lsdvincent@gmail.com',
    license='MIT',
    long_description='https://github.com/lsdlab/avatar-gen',
    install_requires=['pillow==5.0.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent', 'Programming Language :: Python'
    ])
