from Crypto.PublicKey import RSA
from Crypto import Random

from pactplan.interface import IKey


def generate_key() -> IKey:
    key_pair = RSA.generate(4096, Random.new().read)
    return IKey(
        private_key=key_pair.exportKey().decode("utf-8"),
        public_key=key_pair.publickey().exportKey().decode("utf-8")
    )
