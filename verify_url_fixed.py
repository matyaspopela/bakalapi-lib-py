from bakalapi import BakalapiClient

try:
    # This should now fail because base_url is no longer an argument
    client = BakalapiClient("http://custom-url.com")
    print("Failure: BakalapiClient accepted a URL argument, which it shouldn't.")
except TypeError:
    print("Success: BakalapiClient correctly rejected the URL argument.")
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")

try:
    # This should succeed and use the default internal URL
    client = BakalapiClient()
    if client.base_url == "https://bakalapi-production-ed90.up.railway.app/api/timetable":
        print("Success: Default URL is correct.")
    else:
        print(f"Failure: Incorrect default URL: {client.base_url}")
except Exception as e:
    print(f"Unexpected error during default init: {e}")
