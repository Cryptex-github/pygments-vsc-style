from setuptools import setup

setup(
    name='pygments_vsc_style',
    author="Cryptex",
    url='https://github.com/Cryptex-github/pygments-vsc-style',
    project_urls={
        "Issue tracker": "https://github.com/Cryptex-github/pygments-vsc-style/issues",
    },
    version="0.0.1",
    packages=[
        "pygments_vsc_style"
    ],
    license='MIT',
    description='A pygments style inspired by vsc.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'pygments>=2.9.0'
    ],
    entry_points="""
[pygments.styles]
vsc = pygments_vsc_style:VscStyle
    """,
    python_requires='>=3.8.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)