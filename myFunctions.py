from currency_converter import CurrencyConverter
from gtts import gTTS
from playsound import playsound

#variables
converter = CurrencyConverter()

def getCurrency():
  """Prompts user for desired currency.
  """
  currency = input().upper()
  if len(currency) == 3 and currency.isalpha() is True and currency in converter.currencies:
    return currency
  else:
    getCurrency()


def getAmount():
  """Prompts user for amount of money they want to convert.
  """
  amount = input()
  if amount.isdecimal() is True:
    return float(amount)
  else:
    getAmount()


def spellOut(string):
  """Spells the string out.

  Used for spelling out the decimal part of the converted currency.
  """
  if string.isdecimal() is True:
    modified_string = ''
    for character in string:
      modified_string += character + ' '
    return modified_string


def getResult(currency1, currency2, amount, currency_dictionary):
  """Returns the result of the conversion.
  """
  split_amount = str(amount).split('.')
  result = str(converter.convert(amount, currency1, currency2))[:7].split('.')
  curr1 = currency_dictionary[currency1]
  curr2 = currency_dictionary[currency2]
  return (split_amount[0] + ' cijelih ' + spellOut(split_amount[1]) + curr1 + ' iznosi ' + result[0] + ' cijelih ' + spellOut(result[1]) + curr2 + '.')


def talk(string, filename, lang='hr'):
  """Used for playing output strings.
  """
  sound = gTTS(string, lang)
  mp3 = filename + '.mp3'
  sound.save(mp3)
  playsound(mp3)
  print(string)