from setuptools import setup

setup(
    name="maspim_blog",
    version="0.1.0",
    packages=["blog","app_blog"],
    install_requires=[
        "django",
        "django-markdownify",
    ],
)