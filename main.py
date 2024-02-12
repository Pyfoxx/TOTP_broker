from datetime import datetime
import string
import pyotp
from itertools import product


def verify_otp(input_datetime: datetime, secret_key: str, otp_code: str) -> bool:
	"""
	Verify the given OTP code using the secret key and input time.

	:param input_datetime: The datetime object representing the input time for verification.
	:param secret_key: The secret key used for OTP generation.
	:param otp_code: The OTP code to be verified.
	:return: True if the OTP code is valid for the given time and secret key, False otherwise.
	"""
	totp = pyotp.TOTP(secret_key)
	return totp.verify(otp_code, for_time=input_datetime)


def main(key_lenght: int, datetime_moment: [datetime, datetime], otp: [int, int]):
	"""
	:param key_lenght: The length of the key used for generating OTPs.
	:param datetime_moment: A list of two datetime objects representing the moments at which OTPs need to be verified.
	:param otp: A list of two OTPs to be verified.
	:return: Returns 0 after printing the key if both OTPs are verified successfully.

	"""
	all_char = "234567" + string.ascii_lowercase
	generator = product(all_char, repeat=int(key_lenght))
	for p in generator:
		if verify_otp(datetime_moment[0], ''.join(p), otp[0]):
			if verify_otp(datetime_moment[1], ''.join(p), otp[1]):
				print(p)
	return 0


if __name__ == "__main__":
	print(main(key_lenght=32, datetime_moment=[datetime(year=0000, month=0, day=00, hour=00, minute=00, second=00), datetime(year=0000, month=0, day=00, hour=00, minute=00, second=00)], otp=["000000", "000000"]))



