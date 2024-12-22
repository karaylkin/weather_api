from setuptools import setup, find_packages

setup(
    name='weather_api',
    version='0.1.0',
    author='Kara',
    author_email='radmir-lbragimov@mail.ru',
    description='Запрос погоды',
    long_description=open('README.md').read(),
    long_description_content_type='...',
    url='...',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
