"""Zadatak. 
Treba pokupiti tečajnu listu sa weba HNB-a.
Nakon toga treba tečajnu listu pretvoriti u dict, koji
izgleda ovako:

{   'application_date': datetime.date(2016, 11, 9),
    'creation_date': datetime.date(2016, 11, 8),
    'currencies': {   'AUD': (5.21905, 5.234754, 5.250458),
                      ...
                      'HUF': (0.02448132, 0.02455498, 0.02462864),
                      ...
                      'USD': (6.776968, 6.79736, 6.817752)},
    'nr': 216,
    'row_count': 13}

Preporučeno koristiti: datetime.strptime, .decode(), .split(),
    .replace()
"""
from datetime import datetime
import pprint
import urllib3

URL = ('http://www.hnb.hr/hnb-tecajna-lista-portlet/'
       'rest/tecajn/getformatedrecords.dat')


http = urllib3.PoolManager()


def fetch():
    """Run this only if run from command line."""

    response = http.request('GET', URL)

    rows = response.data.decode('utf-8').split('\n')
    header = rows[0]

    data = {
        'nr': int(header[0:3]),
        'creation_date': datetime.strptime(header[3:11], "%d%m%Y").date(),
        'application_date': datetime.strptime(header[11:19], "%d%m%Y").date(),
        'row_count': int(header[19:21]),
        'currencies': dict(),
    }
    currencies = data['currencies']

    for row in rows[1:]:
        key = row[3:6]
        units = int(row[6:9])
        currencies[key] = (float(row[9:24].replace(',', '.')) / units,
                           float(row[24:39].replace(',', '.')) / units,
                           float(row[39:].replace(',', '.')) / units)
    return data


def main():
    """Function is run from console."""
    data = fetch()
    pp = pprint.PrettyPrinter(width=80, indent=4, depth=3)
    pp.pprint(data)

if __name__ == "__main__":
    main()
