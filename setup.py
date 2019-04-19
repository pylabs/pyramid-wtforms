try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyramid_wtforms',
    version='2.5.1',
    packages=['pyramid-wtforms',],
    description='pyramid_wtforms provides bindings for the Pyramid web framework to the WTForms library.',
    author='PyLabs',
    author_email='contact@pylabs.org',
    url='https://github.com/pylabs/pyramid-wtforms',
    license='BSD',
    long_description=open('README.txt').read(),
    install_requires = ['pyramid>=1.5', 'WTForms>=2.1,<3'],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
    ]
)
