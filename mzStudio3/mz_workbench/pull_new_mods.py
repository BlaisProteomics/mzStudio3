
from multiplierz.mzReport import reader, writer

def pull_new_mods(filename, rdr):
    header = {}
    for row in rdr:
        print row
        

filename = r'\\rc-data1.dfci.harvard.edu\blaise\pipeline\ficarro\Ivanov_collab\2020-07-16-monolith_all2\2020-07-15-Monlith-40-675.raw.hcd.xlsx'

rdr = reader(filename, sheet_name = 'Mascot_Header')

pull_new_mods(filename, rdr)