from datetime import datetime

class Event:
    """
    Simple data container; you could switch to
    an ODM (MongoEngine) later if you prefer.
    """
    def __init__(
        self,
        event_type: str,
        author: str,
        timestamp: str | None = None,
        from_branch: str | None = None,
        to_branch: str | None = None,
    ):
        self.event_type = event_type
        self.author = author
        self.from_branch = from_branch
        self.to_branch = to_branch
        self.timestamp = timestamp or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "event_type": self.event_type,
            "author": self.author,
            "from_branch": self.from_branch,
            "to_branch": self.to_branch,
            "timestamp": self.timestamp,
        }
