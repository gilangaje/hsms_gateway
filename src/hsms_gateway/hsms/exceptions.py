"""
Custom exceptions untuk HSMS Gateway.
"""


class HsmsError(Exception):
    """Base exception untuk semua error HSMS."""


class ConnectionClosedError(HsmsError):
    """Remote menutup koneksi."""


class ConnectionTimeoutError(HsmsError):
    """Timeout saat melakukan koneksi."""


class SendTimeoutError(HsmsError):
    """Timeout saat mengirim data."""


class ReceiveTimeoutError(HsmsError):
    """Timeout saat menerima data."""


class InvalidFrameError(HsmsError):
    """Frame HSMS tidak valid."""