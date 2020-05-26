import tokenize
from io import BytesIO
import token
import pandas as pd

source = pd.read_pickle('Python_3.pkl')
print('total data set size:', source.shape)
for sourceIndex, row in source.iterrows():
    sourceCode = row['code']
    count = 0
    for toknum, tokval, start, end, _ in tokenize.tokenize(BytesIO(sourceCode.encode('utf-8')).readline):
        print(sourceIndex, str(count) + "*********************************")
        print("TokenType:", token.tok_name[toknum], '\tToken:', tokval, '\tPosition:', start, end)
        count = count + 1




