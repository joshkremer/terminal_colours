from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Terminal Colours',
    url='https://github.com/joshkremer/terminal_colours',
    author='Josh Kremer',
    author_email='joshkremer@gmail.com',
    # Needed to actually package something
    packages=['terminal_colours'],
    # Needed for dependencies
    # install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An easy way to add colour to the MacOS terminal'
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)