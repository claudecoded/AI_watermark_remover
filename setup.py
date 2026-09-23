from setuptools import setup, find_packages

setup(
    name="watermark-remover",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python tool to remove watermarks from images using OpenCV Inpainting.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
    ],
)
