"""Convert password strings to base64"""
import base64

TEST_STRING = b'Thisbemypassword'

new_b64_string = base64.b64encode(TEST_STRING)
decoded = base64.b64decode(new_b64_string)

print(decoded.decode("utf-8"))
