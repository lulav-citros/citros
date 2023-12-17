# ==============================================
#  ██████╗██╗████████╗██████╗  ██████╗ ███████╗
# ██╔════╝██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝
# ██║     ██║   ██║   ██████╔╝██║   ██║███████╗
# ██║     ██║   ██║   ██╔══██╗██║   ██║╚════██║
# ╚██████╗██║   ██║   ██║  ██║╚██████╔╝███████║
#  ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
# ==============================================

__all__ = []

__version__ = "unknown"
try:
    from citros_meta import (
        __version__,
        __author__,
        __author_email__,
        __copyright__,
        __description__,
        __license__,
        __title__,
        __url__,
    )
except ImportError:
    # We're running in a tree that doesn't have a _version.py, so we don't know what our version is.
    pass
