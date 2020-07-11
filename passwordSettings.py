import enum

class PasswordSettings(enum.Enum):
  NOT_SET = 0
  UPPER_CASE = 1
  LOWER_CASE = 2
  NUMBER = 3
  SPECIAL_CHARACTER = 4
  READABLE_NO_NUMBER = 5
  READABLE_NUMBER = 6
