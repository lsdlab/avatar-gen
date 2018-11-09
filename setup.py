from setuptools import setup, find_packages

setup(
    name='avatar-gen',
    version='1.0.2',
    author="chen Jian",
    author_email="lsdvincent@gmail.com",
    license='MIT',
    description="Using pillow for generate avatars, first letter of string in Chinese and English or random pixel like avatars.",
    packages=find_packages(),
    package_data={'': ['*.otf', 'fonts/*.otf']},
    include_package_data=True,
    install_requires=['pillow'],
    url='https://github.com/lsdlab/avatar-gen',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
)
