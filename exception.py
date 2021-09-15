class ValueTooLargeError(Exception):
    """Raised when input is too large"""
    print("Working days should be less than 30 and hours should be less than 250")


class ValueTooSmallError(Exception):
    """Raised when input is too small"""
    print("Working days should be more than 5 and hours should be more than 50")