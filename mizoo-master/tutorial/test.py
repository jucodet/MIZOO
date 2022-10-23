import base64

# Start your middleware class
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "http://x.botproxy.net:8080"

        # Use the following lines if your proxy requires authentication
        auth_creds = "USERNAME:PASSWORD"
        # setup basic authentication for the proxy
        access_token = base64.encodestring(auth_creds)
        request.headers['Proxy-Authorization'] = 'Basic ' + access_token
