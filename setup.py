from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(name='system-windows',
    version='0.0.1',
    license='MIT License',
    author='Levi Marcomin',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='lelellele531@gmail.com',
    keywords='system-windows',
    description=u'Uma biblioteca para mexer com o arquivos',
    packages=['system-windows'],
    install_requires=[''],)