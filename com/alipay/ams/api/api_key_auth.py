"""Instance-local authentication for ordinary OpenAPI v2 requests."""
import base64
import binascii
import re
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class ApiKeyAuth(object):
    def __init__(self, gateway_url, api_key):
        try:
            gateway = urlparse(gateway_url)
            if (gateway.scheme != "https" or not gateway.hostname or gateway.username
                    or gateway.password or gateway.path not in ("", "/")
                    or gateway.query or gateway.fragment):
                raise ValueError()
            gateway.port
        except (ValueError, TypeError, AttributeError):
            raise ValueError("API Key requires an absolute HTTPS gateway without credentials, path, query or fragment")
        try:
            parts = api_key.split("_", 3)
            if (len(parts) != 4 or parts[0] not in ("isak", "irak")
                    or parts[1] not in ("TEST", "PROD")
                    or not re.match(r"\A[A-Za-z0-9+/]+\Z", parts[2])
                    or not re.match(r"\A[A-Za-z0-9_-]+\Z", parts[3])):
                raise ValueError()
            encoded = parts[2].encode("ascii")
            decoded = base64.b64decode(encoded + b"=" * (-len(encoded) % 4))
            if not decoded or base64.b64encode(decoded).rstrip(b"=") != encoded:
                raise ValueError()
            self.client_id = decoded.decode("utf-8")
        except (ValueError, TypeError, AttributeError, UnicodeError, binascii.Error):
            raise ValueError("Invalid API Key format; expected Standard or Restricted TEST/PROD key")
        self.__key = api_key
        self.__sandbox = parts[1] == "TEST"
        self.gateway_url = gateway_url.rstrip("/")

    def path(self, path):
        if path.startswith("/ams/sandbox/api/"):
            path = "/ams/api/" + path[len("/ams/sandbox/api/"):]
        if not path.startswith("/ams/api/") or "?" in path or "#" in path:
            raise ValueError("API Key requires an ordinary /ams/api/ request path")
        return path.replace("/ams/api/", "/ams/sandbox/api/", 1) if self.__sandbox else path

    def authorization(self):
        return "Bearer " + self.__key
