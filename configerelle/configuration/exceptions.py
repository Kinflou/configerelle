# Standard Import

# Local Imports

# External Imports


class SegmentNotFoundError(Exception):

    def __init__(self, missing: str, rest: list[str]):
        self.missing = missing
        self.rest = rest

    def __str__(self):
        return f"Segment '{self.missing}' does not exist in {'.'.join(self.rest)}"

