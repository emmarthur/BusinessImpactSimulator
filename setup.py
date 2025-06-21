from setuptools import setup, find_packages

setup(
    name="business_impact_simulator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "crewai>=0.11.0",
        "langchain>=0.1.0",
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
        "pydantic>=2.6.0",
        "python-dotenv>=1.0.0",
        "pandas>=2.2.0",
        "numpy>=1.26.0",
        "scikit-learn>=1.4.0",
        "matplotlib>=3.8.0",
        "seaborn>=0.13.0",
        "pytest>=8.0.0",
        "python-multipart>=0.0.9",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A system for simulating business impact across different domains",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/business_impact_simulator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
