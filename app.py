import myFunctions

# main loop
if __name__ == '__main__':
  all_currencies = {
  'HRK': 'Hrvatskih kuna',
  'USD': 'Američkih dolara',
  'AUD': 'Australskih dolara',
  'CAD': 'Kanadskih dolara',
  'EUR': 'Eura',
  'GBP': 'Funta',
  'INR': 'Indijskih rupija',
  'JPY': 'Japanskih jena',
  'RON': 'Rumunjskih leua',
  'KRW': 'Južnokorejskih vona',
  'EEK': 'Estonskih kruna',
  'SEK': 'Švedskih kruna',
  'THB': 'Tajlandskih bahta',
  'HUF': 'Mađarskih forinta',
  'MXN': 'Meksičkih pezoa',
  'ROL': 'Rumunjskih leua',
  'TRY': 'Turskih lira',
  'CHF': 'Švicarskih franaka',
  'DKK': 'Danskih kruna',
  'PHP': 'Filipinskih pezoa',
  'ISK': 'Islandskih kruna',
  'SKK': 'Slovačkih kruna',
  'CYP': 'Ciparskih funta',
  'HKD': 'Hongkonških dolara',
  'NOK': 'Norveških kruna',
  'SGD': 'Singapurskih dolara',
  'SIT': 'Slovenskih tolara',
  'CNY': 'Kineskih juana',
  'CZK': 'Čeških kruna',
  'PLN': 'Poljskih zlota',
  'IDR': 'Indonezijskih rupija',
  'ILS': 'Novih Izraelskih šekela',
  'BRL': 'Brazilskih reala',
  'ZAR': 'Južnoafričkih randa',
  'RUB': 'Ruskih rubalja',
  'BGN': 'Bugarskih leva',
  'MTL': 'Malteških lira',
  'LVL': 'Letonskih latasa',
  'TRL': 'Turskih lira',
  'LTL': 'Litavski litasa',
  'MYR': 'Malezijskih ringita',
  'NZD': 'Novozelandskih dolara'
  }
  
  myFunctions.talk('Unesite prvu valutu.', 'currency1_file')
  currency1 = myFunctions.getCurrency()

  myFunctions.talk('Unesite drugu valutu.', 'currency2_file')
  currency2 = myFunctions.getCurrency()

  myFunctions.talk(f'Koliko {all_currencies[currency1]} želite zamijeniti?', 'amount_file')

  amount = myFunctions.getAmount()

  result = myFunctions.getResult(currency1, currency2, amount, all_currencies)

  myFunctions.talk(result, 'result_file')