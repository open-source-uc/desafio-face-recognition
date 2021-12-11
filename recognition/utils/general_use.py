import base64


def encode_base64_password(password: str):
    message = password
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_password = base64_bytes.decode("ascii")
    return base64_password
