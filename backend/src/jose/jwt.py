import hmac
import hashlib
import base64
import json
import time

# Minimal JWT encode/decode using HMAC-SHA256. Not security hardened — used for tests only.

def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(s: str) -> bytes:
    padding = '=' * (-len(s) % 4)
    return base64.urlsafe_b64decode(s + padding)


def encode(payload: dict, secret: str, algorithm: str = "HS256") -> str:
    header = {"alg": algorithm, "typ": "JWT"}
    header_b64 = _b64url_encode(json.dumps(header, separators=(',', ':')).encode('utf-8'))
    payload_b64 = _b64url_encode(json.dumps(payload, separators=(',', ':')).encode('utf-8'))
    signing_input = f"{header_b64}.{payload_b64}".encode('utf-8')
    if algorithm != "HS256":
        raise NotImplementedError("Only HS256 supported in test jwt stub")
    sig = hmac.new(secret.encode('utf-8'), signing_input, hashlib.sha256).digest()
    sig_b64 = _b64url_encode(sig)
    return f"{header_b64}.{payload_b64}.{sig_b64}"


def decode(token: str, secret: str, algorithms: list[str]) -> dict:
    try:
        header_b64, payload_b64, sig_b64 = token.split('.')
    except ValueError:
        raise ValueError("Invalid token format")
    signing_input = f"{header_b64}.{payload_b64}".encode('utf-8')
    expected_sig = hmac.new(secret.encode('utf-8'), signing_input, hashlib.sha256).digest()
    if not hmac.compare_digest(_b64url_decode(sig_b64), expected_sig):
        raise ValueError("Invalid token signature")
    payload_json = _b64url_decode(payload_b64).decode('utf-8')
    payload = json.loads(payload_json)
    exp = payload.get('exp')
    if exp and int(time.time()) > int(exp):
        raise ValueError("Token has expired")
    return payload
