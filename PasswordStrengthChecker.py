import re

def check_length(password):
  """
  Checks if the password meets the minimum length requirement.

  Args:
      password: The password to check (string).

  Returns:
      True if the password meets the minimum length, False otherwise.
  """
  return len(password) >= 8

def check_character_types(password):
  """
  Checks if the password contains at least one uppercase letter, lowercase letter, number, and special symbol.

  Args:
      password: The password to check (string).

  Returns:
      True if the password meets all character type requirements, False otherwise.
  """
  has_uppercase = re.search("[A-Z]", password)
  has_lowercase = re.search("[a-z]", password)
  has_number = re.search("[0-9]", password)
  has_symbol = re.search("[!@#$%^&*(),.?]", password)
  return has_uppercase and has_lowercase and has_number and has_symbol

def check_strength(password):
  """
  Analyzes password strength based on length and character types.

  Args:
      password: The password to check (string).

  Returns:
      A tuple containing the strength score (integer) and a message (string).
  """
  score = 0
  message = ""
  if check_length(password):
    score += 1
  else:
    message += "Password is too short. Minimum length is 8 characters.\n"
  if check_character_types(password):
    score += 3
  else:
    message += "Password should include uppercase letters, lowercase letters, numbers, and special symbols.\n"
  strength = "Weak"
  if score == 4:
    strength = "Strong"
  elif score == 3:
    strength = "Moderate"
  return score, f"Password Strength: {strength}\n{message}"

def main():
  password = input("Enter your password: ")
  score, message = check_strength(password)
  print(message)

if __name__ == "__main__":
  main()
