# Meter event upload

Install the optional HTTP/2 dependencies. This API requires Python 3.9 or later;
other SDK APIs retain the package's existing Python compatibility.

```bash
pip install "global-open-sdk-python[http2]"
```

`meter/createSession` uses the regular signed AMS transport. Use its session ID
to call `meter/uploadEvent` through `execute_with_headers`:

```python
# Requires Python 3.9+ and: pip install "global-open-sdk-python[http2]"
request = AlipayMeterUploadEventRequest()
request.meters = meters
response_body = default_alipay_client.execute_with_headers(
    request, {"X-Session-Id": session_id}
)
```

The SDK sends `meter/uploadEvent` to the gateway URL configured on the client,
without sandbox path rewriting, request signing, response signature verification,
or automatic retries. This API requires HTTP/2.
