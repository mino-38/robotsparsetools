from setuptools import setup

with open("./README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="robotsparsetools",
    description="Parse robots.txt",
    long_description=long_description,
    version="1.0.0",
    author="minomushi",
    author_email="mino3@cocoro.uk",
    url="https://github.com/mino-38/robotsparsetools",
    packages=["robotsparsetools"],
    keywords="robots.txt parser",
    licence="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only"
    ]
)