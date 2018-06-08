from setuptools import setup


setup(
    name='pyquakeml',
    description='PyQuakeML: Lightweight QuakeML data parsing for Python',
    url='https://git.gfz-potsdam.de/nooshiri/pyquakeml',
    author='Nima Nooshiri; Sebastian Heimann',
    author_email='nima.nooshiri@gfz-potsdam.de; '
                 'sebastian.heimann@gfz-potsdam.de',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering'],
    install_requires=['pyyaml>=3.11', 'guts>=0.2'],
    package_dir={'': 'src'},
    py_modules=['pyquakeml'])
