from setuptools import setup

setup(
    name='wordsegmenterTC',
    version='0.1',
    description='Wordsegmenter using PyICU.',
    author='Thodsaporn Chay-intr',
    author_email='t.chayintr@icloud.com',
    url='https://github.com/tchayintr/wordsegmenterTC',
    packages=["wordsegmenterTC"],
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
    ],
)