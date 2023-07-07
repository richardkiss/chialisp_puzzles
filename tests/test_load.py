from chialisp_puzzles import load_puzzle


def check(puzzle_name: str, expected_hash: str):
    program = load_puzzle(puzzle_name)
    assert program.tree_hash().hex() == expected_hash


def test_load():
    check(
        "p2_delegated_puzzle_or_hidden_puzzle",
        "e9aaa49f45bad5c889b86ee3341550c155cfdd10c3a6757de618d20612fffd52",
    )
    check(
        "p2_conditions",
        "1c77d7d5efde60a7a1d2d27db6d746bc8e568aea1ef8586ca967a0d60b83cc36",
    )
    check(
        "calculate_synthetic_public_key",
        "624c5d5704d0decadfc0503e71bbffb6cdfe45025bce7cf3e6864d1eafe8f65e",
    )
