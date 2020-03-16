from setuptools import setup, Extension, find_packages
import os

setup(
    name="travis_test",
    description="-",
    author="K0lb3",
    version="0.9.0",
    keywords=['astc', 'atc', 'pvrtc', "etc", "crunch"],
    url="https://github.com/K0lb3/travis_test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=[
        Extension(
            "travis_test",
            [
                os.path.join(root, f)
                for root, dirs, files in os.walk("src")
                for f in files
            ],
            language="c++",
            extra_compile_args=["-std=c++11"]
        )]
)
