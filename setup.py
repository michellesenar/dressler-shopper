from setuptools import find_packages, setup

requirements = [
    "bs4",
    "python-dotenv",
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
    entry_points={
        "console_scripts": [
            "cliq = shopper.cliq:main",
            "text = shopper.sms:main",
        ],
    },
)
