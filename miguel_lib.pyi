from typing import List, Optional, Tuple

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]: ...
def utf16len(string: str) -> int: ...

class Interval:
    def __init__(self, interval_list: Optional[List[Tuple[int, int]]]) -> None: ...
    def __contains__(self, item: int) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
