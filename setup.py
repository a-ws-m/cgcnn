from setuptools import setup, find_packages

setup(
    name="Modular CGCNN",
    version="1.0.1",
    url="https://github.com/a-ws-m/cgcnn.git",
    author="Tian Xie; Alexander Moriarty",
    description="Crystal Graph Convolutional Neural Networks with a modular design.",
    packages=find_packages(),
    install_requires=["pytorch", "scikit-learn", "torchvision", "pymatgen"],
)
