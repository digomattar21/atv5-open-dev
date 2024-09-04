from setuptools import setup

setup(
    name='dev_aberto_rodrigomattar',
    version='0.1',
    packages=['dev_aberto'],
    author='Your Name',
    python_requires='>=3',
    classifiers=[
        'Operating System :: OS Independent',
    ],
    install_requires=["requests"],
    scripts=['scripts/hello.py'],
)
