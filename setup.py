"""Setup to install TensorFlow Model Remediation package."""

from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'six',
    'tensorflow>=2.0.0',
]

# Get version from version module.
with open('version.py') as fp:
  globals_dict = {}
  exec(fp.read(), globals_dict)  # pylint: disable=exec-used
__version__ = globals_dict['__version__']

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
    name='tensorflow_model_remediation',
    version=__version__,
    description='TensorFlow Model Remediation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tensorflow/model-remediation',
    author='Google LLC',
    author_email='packages@tensorflow.org',
    packages=find_packages(),
    python_requires='>=3.6,<4',
    install_requires=REQUIRED_PACKAGES,
    tests_require=REQUIRED_PACKAGES,
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='Apache 2.0',
    keywords='tensorflow model remediation fairness responsible machine learning',
)