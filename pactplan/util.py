from Crypto.PublicKey import RSA
from Crypto import Random


def generate_key() -> dict:
    key_pair = RSA.generate(4096, Random.new().read)
    return {
        "private_key": key_pair.exportKey().decode("utf-8"),
        "public_key": key_pair.publickey().exportKey().decode("utf-8")
    }
