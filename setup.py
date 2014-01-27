from pip.req import parse_requirements
from setuptools import setup, find_packages
from dexy.version import DEXY_VERSION

install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

setup(
        author='Ana Nelson',
        author_email='ana@ananelson.com',
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Financial and Insurance Industry",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Topic :: Documentation",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Software Development :: Code Generators",
            "Topic :: Software Development :: Documentation",
            "Topic :: Text Processing",
            "Topic :: Text Processing :: Markup :: HTML",
            "Topic :: Text Processing :: Markup :: LaTeX"
            ],
        description='Document Automation',
        ### "entry-points"
        entry_points = {
            'console_scripts' : [
                'dexy = dexy.commands:run'
                ],
            'pygments.lexers' : [
                'rst+django = dexy.filters.utils:RstDjangoLexer'
                ]
            },
        ### @end
        include_package_data = True,
        install_requires=reqs,
        name='dexy',
        packages=find_packages(),
        url='http://dexy.it',
        version=DEXY_VERSION
    )
