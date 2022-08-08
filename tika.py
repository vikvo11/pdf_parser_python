from tika import parser # pip install tika

raw = parser.from_file('test_tables.pdf')
print(raw['content'])
