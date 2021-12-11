from recognition.utils.general_use import encode_base64_password


def nc200_connection_url(user: str, password: str, host: str, port: int):
    base64_password = encode_base64_password(password)
    camera_url = f"http://{user}:{base64_password}@{host}:{port}/stream/getvideo"
    return camera_url
