def find_highest_frequency(s):
  # Create a dictionary to store the character frequencies
  char_frequencies = {}

  # Count the frequency of each character in the string
  for c in s:
    if c in char_frequencies:
      char_frequencies[c] += 1
    else:
      char_frequencies[c] = 1

  # Find the character with the highest frequency
  highest_frequency = 0
  highest_frequency_char = None
  for c, frequency in char_frequencies.items():
    if frequency > highest_frequency:
      highest_frequency = frequency
      highest_frequency_char = c

    # Return the character with the highest frequency
  return highest_frequency_char

# Prompt the user to enter a string

s = input("Enter a string: ")

# Test the function with a few strings

print(find_highest_frequency(s))  







