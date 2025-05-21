import random
import string


def generate_video_id():
    allowed_chars = string.ascii_letters + string.digits + "_-"
    return "".join(random.choices(allowed_chars, k=11))
