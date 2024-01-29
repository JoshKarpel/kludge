from __future__ import annotations


def clamp(min_: int, val: int, max_: int) -> int:
    return max(min_, min(val, max_))
