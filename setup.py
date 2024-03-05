import setuptools
setuptools.setup(
    name="StudentCopilot",
    version="1.0.0",
    description="Transcript audio files",
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Tommaso Califano",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    py_modules=["simpleUI", "StudentCopilot"],
    include_package_data=True,
    install_requires=setuptools.find_packages(),
    entry_points={"console_scripts": ["StudentCopilot=reader.__main__:main"]},
)