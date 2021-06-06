from setuptools import find_packages, setup

requirements = [
    "bs4",
    "requests",
    "twilio",
]

setup(
    name="dressler_shopper",
    version="0.1",
    description="Collection of scripts to check if product(s) in stock",
    url="https://github.com/michellesenar/dressler-shopper",
    author="Michelle Senar Dressler",
    license="MIT",
    install_requires=requirements,
    packages=find_packages("src"),
    package_dir={"": "src"},
)
