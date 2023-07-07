# Starter SConstruct for enscons

import enscons
import pytoml
from runtime_builder import build_all_items_for_package

BASE_PACKAGE = "chialisp_puzzles"

metadata = dict(pytoml.load(open("pyproject.toml")))["project"]

full_tag = "py3-none-any"  # pure Python packages compatible with 2+3

env = Environment(
    tools=["default", "packaging", enscons.generate],
    PACKAGE_METADATA=metadata,
    WHEEL_TAG=full_tag,
    ROOT_IS_PURELIB=full_tag.endswith("-any"),
)

py_source = Glob(f"{BASE_PACKAGE}/*.py")

sdist_source = (
    File(["PKG-INFO", "README.md", "SConstruct", "pyproject.toml"]) + py_source
)
sdist = env.SDist(source=sdist_source)

built_items = build_all_items_for_package("chialisp_puzzles.puzzles")
# convert `Path` to `str` as scons can't handle `Path` objects
built_items_str = [str(_) for _ in built_items]

wheel_contents = py_source + built_items_str

wheel_metadata = env.Whl("purelib", wheel_contents, root="")
wheel = env.WhlFile(source=wheel_metadata)

env.NoClean(sdist)
env.Alias("sdist", sdist)

# needed for pep517 (enscons.api) to work
env.Default(wheel, sdist)
