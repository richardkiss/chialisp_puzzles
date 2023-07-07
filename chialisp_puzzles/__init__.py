from clvm_rs import Program


def load_puzzle(puzzle_name: str) -> Program:
    from chialisp_loader import load_program

    return load_program("chialisp_puzzles.puzzles", f"{puzzle_name}.hex")
