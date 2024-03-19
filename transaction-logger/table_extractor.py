from tabula.io import read_pdf

path = "/Users/shreysharma/Downloads/transactions.pdf"

df = read_pdf(path, pages='all')

print(df[0])



# this is a new comment added into new clone