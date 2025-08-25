import setuptools

with open("README.rst") as f:
    long_description = f.read()

setuptools.setup(
    name="pytest-twisted",
    version="1.14.4+tfw",
    description="Fork of pytest-twisted for internal use",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Ralf Schmitt, Kyle Altendorf, Victor Titor",
    author_email="sda@fstab.net",
    url="https://github.com/thefourthway/pytest-twisted",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*',
    install_requires=["greenlet", "pytest>=2.3", "decorator"],
    extras_require={
        "dev": ["pre-commit", "black"],
        "pyside2": [
            # >= 0.6.3 for PySide2 extra version constraints
            "qt5reactor[pyside2]>=0.6.3",
        ],
        "pyqt5": ["qt5reactor[pyqt5]>=0.6.2"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",  
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={"pytest11": ["twisted = pytest_twisted"]},
)
