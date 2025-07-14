# event.py
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class Event:
    """Lightweight container for webhook events."""

    event_type: str
    author: str
    timestamp: str = datetime.utcnow().isoformat()
    from_branch: Optional[str] = None
    to_branch: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

