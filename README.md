# chialisp_puzzles

This project contains several standard and legacy puzzles commonly used on the chia network.

Note that it uses `enscons` to build, as the more commonly used `setuptools` does not easily allow fine-grained control of the contents of the `sdist` and `wheel` files.

In particular, this example takes pains to include the source files `runtime_build` or `*.clsp` in the sdist but not the wheel.

## Use

To load a puzzle, do something like

```python
from chialisp_puzzles import load_puzzle

program = load_puzzle("p2_delegated_puzzle_or_hidden_puzzle")
```

## License
- This project is licensed under the Apache 2 License. See the LICENSE file for more details.
