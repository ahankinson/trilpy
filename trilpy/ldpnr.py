"""An LDPNR - Non-RDF Source."""
from trilpy.ldpr import LDPR

class LDPNR(LDPR):
    """LDPNR - 

    An LDPR whose state is not represented in RDF. For example,
    these can be binary or text documents that do not have useful
    RDF representations.

    See <https://www.w3.org/TR/ldp/#ldpnr>.
    """

    def __init__(self, content=None, media_type=None):
        """Initialize LDPNR."""
        self.content = content
        self.type = media_type
        