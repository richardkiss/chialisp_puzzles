from setuptools import setup, find_packages
from runtime_builder import build_runtime_setuptools


setup(
    packages=["chialisp_puzzles", "chialisp_puzzles.puzzles"],
    package_data={"chialisp_puzzles.puzzles": ["*.hex", "*.clsp", "runtime_build"]},
    cmdclass={
        "build_runtime_builder_artifacts": build_runtime_setuptools("chialisp_puzzles.puzzles"),
    },
)
