from . import settings


def center(width, height):
    return \
        (
            (settings.SCREEN_WIDTH - width) / 2,
            (settings.SCREEN_HEIGHT - height) / 2
        )
