class Plugin:
    """
    This class represent for a Plugin. A plugin is a small program do a assigned work, such as finding sub-domain,
    but it should be very specific
    """

    def __init__(self):
        self.requester = None
        self.base_url = None
        self.base_domain = None
        self.kb = None

    def get_name(self):
        return self.__class__.__name__

    def add(self, *args):
        """
        Add data to knowledge base
        """
        msg = 'Plugin is not implementing required method add'
        raise NotImplementedError(msg)

    def get_type(self):
        return 'plugin'

    def set_requester(self, requester):
        self.requester = requester
        if self.requester is not None:
            self.setup_http()

    def set_kb(self, kb):
        self.kb = kb

    def setup_http(self):
        """
        I think we will need this method. It support modify the http request header
        """
        pass
