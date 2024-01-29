from __future__ import annotations

from datetime import datetime, timezone


def clamp(min_: int, val: int, max_: int) -> int:
    return max(min_, min(val, max_))


def now() -> datetime:
    return datetime.now(timezone.utc)
