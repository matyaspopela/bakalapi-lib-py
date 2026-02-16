from bakalapi import BakalapiClient

try:
    client = BakalapiClient()
    print("Success: BakalapiClient() initialized without arguments.")
except TypeError as e:
    print(f"Failure: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
