import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "readme.md").read_text(encoding="utf-8")

setup(
    name="fastapi-route-logger-middleware",
    version="0.1.0",
    description="Simple middleware for FastAPI to generate log entries on all requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffsiver/fastapi-route-logger",
    author="Jeff Siver",
    author_email="jeffsiver@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="fastapi, logging, middleware",
    packages=["fastapi_route_logger_middleware"],
    python_requires=">=3.7",
    install_requires=["fastapi"],
)
