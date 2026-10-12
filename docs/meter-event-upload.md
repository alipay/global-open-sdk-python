# Meter event upload

Use Python 3.9.2 or later, as described in [Installation](../README.md#installation),
and install the optional HTTP/2 dependencies:

```bash
python -m pip install --upgrade "global-open-sdk-python[http2]"
```

`meter/createSession` uses the regular signed AMS transport. Use its session ID
to call `meter/uploadEvent` through `execute_with_headers`:

```python
# Requires the http2 extra installed above.
request = AlipayMeterUploadEventRequest()
request.meters = meters
response_body = default_alipay_client.execute_with_headers(
    request, {"X-Session-Id": session_id}
)
```

The SDK sends `meter/uploadEvent` to the gateway URL configured on the client,
without sandbox path rewriting, request signing, response signature verification,
or automatic retries. This API requires HTTP/2.
