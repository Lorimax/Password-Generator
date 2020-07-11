import enum

class PasswordSettings(enum.Enum):
  UPPER_CASE = 0
  LOWER_CASE = 1
  NUMBER = 2
  SPECIAL_CHARACTER = 3
  READABLE_NO_NUMBER = 4
  READABLE_NUMBER = 5
