def main(filepath):
  with open(filepath) as f:
    book = f.read()

    letter_count = count_letters(book)
    letters_list = list(letter_count.items())
    letters_list.sort(key=sort_func, reverse=True)
    print(f"--- Begin report of {filepath} ---")
    print(f"{count_words(book)} words found in the document\n")
    for letters in letters_list:
      if (letters[0].isalpha()):
        print(f"The character {letters[0]} was found {letters[1]} times.")
    print("--- End report ---")



def sort_func(tuple):
  return tuple[1]

def count_words(string):
  return len(string.split())

def count_letters(string):
  string = string.lower()
  dict = {}
  for letter in string:
    if letter in dict:
      dict[letter] += 1
    else:
      dict[letter] = 1
  return dict

if __name__ == "__main__":
  main("books/frankenstein.txt")