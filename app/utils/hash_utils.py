from argon2 import PasswordHasher


def creation_hash(text: str) -> str:
    ph = PasswordHasher()

    hash = ph.hash(text)

    return hash


def validation_hash(hash: str, text: str) -> bool:
    try:
        ph = PasswordHasher()

        return ph.verify(hash, text)
    except:
        return False
