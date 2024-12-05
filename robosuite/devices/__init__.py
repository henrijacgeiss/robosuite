from .device import Device
from .keyboard import Keyboard

try:
    from .spacemouse import SpaceMouse
except ImportError:
    print(
        """Unable to load module hid, required to interface with SpaceMouse."""
    )
