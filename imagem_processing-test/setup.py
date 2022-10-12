from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="imagem-processing-test",
    version="0.0.1",
    author="Ricardo Francisco da Silva",
    author_email="ricardo20sp@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ricardo-IA/Processamento_imagem",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)