def pad(plaintext: bytes, block_size: int) -> bytes:
    padding = block_size - (len(plaintext) % block_size)
    return plaintext + bytes([padding]) * padding

def unpad(padded: bytes, block_size: int) -> bytes:
    length = len(padded)
    if length % block_size:
        raise ValueError("Input data is not padded")
    if not _is_valid_padding(padded):
        raise ValueError("Not valid padding")
    return padded[:-padded[-1]]

def _is_valid_padding(padded: bytes) -> bool:
    pad = padded[-1]
    return padded[-pad:] == bytes([pad]) * pad