# Antom SDK for Python

Latest release: **1.6.1**

## Installation

```sh
python -m pip install --upgrade global-open-sdk-python
```

Use Python 3 for the examples below.

## Quick start

- **API Key:** follow the [setup guide](docs/api-key-client.md) and run the [sandbox example](example/api_key_payment_session.py).
- **RSA:** start with the [payment example](example/payment.py).
- Browse [more examples](example) and the [API documentation](https://global.alipay.com/docs/).

API Key and RSA clients share request/response models. File uploads and notification
verification still require RSA credentials.

## Upgrade notes

Gateway responses with `resultStatus S` must be signed; responses with only one
of the signature and response-time headers are rejected.

Billing integrations: `availableAmount` now uses `Amount`; the `AvailableAmount`
model has been removed.

## Meter event upload

`meter/uploadEvent` requires HTTP/2 and `X-Session-Id`. See the
[usage and requirements](docs/meter-event-upload.md).

## Support

For integration questions, contact overseas_support@service.alibaba.com.
