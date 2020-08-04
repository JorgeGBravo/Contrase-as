import hashlib

def encript():
    bytetable = str.encode(aencript)
    print(bytetable)
    table = hashlib.sha256(bytetable).hexdigest()
    print(table)
    decriptar = reversed(table)

