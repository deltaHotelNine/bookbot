def get_book_content(path):
  with open(path) as f:
    return f.read()

def get_book_word_count(text):
  words = text.split()
  return len(words)

def get_char_dict(text):
  char_dict = {}
  text = text.lower()
  for char in text:
    if char in char_dict and char.isalpha():
      char_dict[char] += 1
    else:
      if char.isalpha():
        char_dict[char] = 1
  return char_dict

def sort_on(dict):
  return dict["num"]

def get_char_sorted_list(char_dict):
  char_list = []
  for char, num in char_dict.items():
    char_list.append({"char": char, "num": num})
  char_list.sort(reverse=True, key=sort_on)
  return char_list

def get_report(path, wc, chars):
  report = ""
  report += f"--- Building report for {path} ---\n"
  report += f"{wc} words were found within this book\n\n"
  for char in chars:
    report += f"The character '{char['char']}' was found {char['num']} times\n"
  report += "\n--- End of report ---"
  return report

def main():
  book_path = "books/frankenstein.txt"
  
  text = get_book_content(book_path)
  word_count = get_book_word_count(text)  
  char_dict = get_char_dict(text)
  char_list = get_char_sorted_list(char_dict)
  report = get_report(book_path, word_count, char_list)

  print(report)

main()