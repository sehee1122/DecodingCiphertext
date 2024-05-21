from collections import Counter

def calculate_alphabet_frequency(input_string):
  alphabet_frequency = {}

  for char in input_string:
    if char.isalpha():
      if char in alphabet_frequency:
        alphabet_frequency[char] += 1
      else:
        alphabet_frequency[char] = 1

  sorted_alphabet_frequency = sorted(alphabet_frequency.items(),
                                     key=lambda x: x[1],
                                     reverse=True)

  freq_letter = "etaoinshrdlcumwfgypbvkj"
  num = 0

  for char, frequency in sorted_alphabet_frequency:
    print(f"{char}: {frequency}", freq_letter[num])
    num += 1
  print('\n')

  # etaoinshrdlcumwfgypbvkjq
  mapping = {
      sorted_alphabet_frequency[i][0]: "etaoinshrdlcumwfgypbvkj"[i]
      for i in range(len(sorted_alphabet_frequency))
  }

  result_string = "".join(
      [mapping[char] if char in mapping else char for char in input_string])

  return result_string

def top_grams_frequency(input_string):
  # 문자열에서 알파벳만 추출
  #  alpha_string = ''.join(filter(str.isalpha, input_string.lower()))

  trigrams = [input_string[i:i + 3] for i in range(len(input_string) - 2)]
  #  eightgrams = [input_string[i:i + 8] for i in range(len(input_string) - 7)]

  gram_counts = Counter(trigrams)
  result = gram_counts.most_common(12)

  return result

def map_alphabet(input_string):
  # 알파벳 매핑
  alphabet_mapping = {
      'a': 'a',
      'b': 'o',
      'c': 'd',
      'd': '*',
      'e': 'f',
      'f': 'p',
      'g': 'u',
      'h': 's',
      'i': 'c',
      'j': 'g',
      'k': 'i',
      'l': '*',
      'm': 'y',
      'n': 't',
      'o': '*',
      'p': 'n',
      'q': 'x',
      'r': 'b',
      's': 'k',
      't': 'h',
      'u': 'v',
      'v': 'm',
      'w': 'l',
      'x': 'e',
      'y': 'w',
      'z': 'r'
  }

  for char in alphabet_mapping:
    if char.isupper():
      alphabet_mapping = '*'
    else:
      pass

  result_string = ''

  for char in input_string:
    if char.isalpha():
      result_string += alphabet_mapping[char]
    else:
      result_string += char

  return result_string

def caesar_cipher(text, shift):
  result = ''
  for char in text:
    #    if char.isalpha():
    shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    result += shifted_char
  return result

ciphertext = "izbhhekn kh a tkjt kpnxphknm xqxzikhx fzbjzav yknt itawwxpjkpj txaznfgvfkpj vbuxvxpnh apc ybzsbgnh ntan itapjx yknt xait hxhhkbp jxpxzawwm izbhhekn ybzsbgnh kpiwgcx egpinkbpaw xqxzikhxh ntan faznkikfapnh ibvfwxnx ykntkp a pgvrxz be zbgpch a nkvxwkvkn bz a ixznakp ckhnapix hamh hnxftapx zbitxn a ixznkekxc izbhhekn wxuxw ntzxx nzakpxz apc hxpkbz ibpnxpn yzknxz ebz izbhheknh xcgiankbp cxfaznvxpn izbhhekn ybzsbgn vbuxvxpnh vamrx cxzkuxc ezbv hfbznh wksx bwmvfki jmvpahnkih yxkjtn wkenkpj apc zgppkpj hfxikeki izbhhekn ainkuknkxh uazm cxfxpckpj bp ntx jmv bz wbiankbp tby xuxz hbvx xwxvxpnh zxvakp ibphkhnxpn kp aww wbiankbph hgit ah ntx ybzsbgn be ntx cam a hxzkxh be bpx nb hkq tkjt kpnxphknm xqxzikhxh fbhnxc cakwm nb izbhheknh yxrhknx a nmfkiaw izbhhekn iwahh ibphkhnh be a hnzgingzxc yazv gf a hnzxpjnt apc hskwwh ibvfbpxpn ntx ybzsbgn be ntx cam apc a ibbw cbyp nb zxngzp ntx txazn zanx nb rahxwkpx wxuxwh hamh itzkhnkpx vaza ahfbznh iwkpkiaw hfxikawkhn apc ftmhkiaw ntx zafkhn an bzwapcb txawnt kp ewbzkca"

result1 = calculate_alphabet_frequency(ciphertext)
#print('\n', result1)

result2 = top_grams_frequency(ciphertext)
for ngram, frequency in result2:
  print(f"trigrams: {ngram}, ({frequency} times)", end=', ')

result3 = map_alphabet(ciphertext)
print('\n', result3)

shift = 17

result4 = caesar_cipher(ciphertext, shift)
#print('\n', result4)
