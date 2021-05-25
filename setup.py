import setuptools


setuptools.setup(
    name='changgelog',
    version='0.0.1',
    author='RimoChan',
    author_email='the@librian.net',
    description='changgelog',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/changgelog',
    packages=[
        'changgelog',
    ],
    classifiers=[
        'Environment :: Win32 (MS Windows)',
        'Programming Language :: Python :: 3',
    ],
)