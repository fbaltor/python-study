import os


files = os.listdir('example')

for fname in files:
    if fname.endswith('.pdf'):
        print('PDF file exists')
