from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# Define ROOT DIRECTORY
# Hello world
ROOT_DIR = Path(__file__).resolve().parent.absolute()
FRAME_RATE = 60

CAMERA_USER: str = env("CAMERA_USER")
CAMERA_PASSWORD: str = env("CAMERA_PASSWORD")
CAMERA_IP: str = env("CAMERA_IP")
CAMERA_PORT: int = env("CAMERA_PORT")
