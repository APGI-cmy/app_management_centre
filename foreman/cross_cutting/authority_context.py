"""
Authority Context.
QA Coverage: QA-158
"""


class AuthorityContext:
    """Represents authority context for permission checks."""
    
    def __init__(self, user_id: str, role: str, permissions: list[str]):
        self.user_id = user_id
        self.role = role
        self.permissions = permissions
