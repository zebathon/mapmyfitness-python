class APIConfig(object):
    uri_root = 'https://oauth2-api.mapmyapi.com'
    api_root = '{0}/v7.0'.format(uri_root)

    def __init__(self, api_key, access_token, uri_root=None, version=None):
        from nose.tools import set_trace; set_trace()

        self.api_key = api_key
        self.access_token = access_token
        if uri_root:
            self.uri_root = uri_root
        if version:
            self.version = version
            self.api_root = '{0}/{1}'.format(self.uri_root, version)
