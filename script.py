
import re
import numpy as np
from tika import parser
import pandas as pd  
import os
from pathlib import Path

def stringToWords(string):
    string = string.lower()
    words = re.findall(r'[a-zA-Z]+', string)
    words = np.unique(words) 
    words.sort()
    return words
    
path = str(input("Enter your file path: "))
document = parser.from_file(path)
content = document['content']
words = stringToWords(content)
downloadPath = os.path.join(Path.home(), "Documents", "words.csv")
dataframe = pd.DataFrame(words)
dataframe.to_csv(path_or_buf=downloadPath, header=False, index=False)


