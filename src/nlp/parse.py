import unicodedata # for function remove_accented_chars
from tqdm import tqdm # for pogress bar on a loop inside a function


def remove_accented_chars(text):
    """Turns accented characters i.e. é, ä into unaccented characters ie e, a, in a string

    Args: 
      text: string containing any characters

    Returns: same string, with any accented characters replaced

    """
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text



def strip_most_punc(df, column):
    """Deletes most common symbols from a string.
    Does not delete the following strings ' : ; () ! ? # %
    Comes with progress bar built in. 

    Args: 
      df: name of dataframe
      column: name of a column from the dataframe 

    Returns: same string in the same position within the df, with listed characters removed

    """
    punc = str.maketrans('', '', '-[]{}",<>./@^&*_~')
    for row in tqdm(range(len(df))):
        df.loc[row,column] = df.loc[row,column].translate(punc)



def strip_apostrophe(df, column):
    """Deletes apostrophes wherever they appear in strings in a dataframe column. 

    Args: 
      df: name of dataframe
      column: name of a column from the dataframe 

    Returns: same string in the same position within the df, with apostrophes removed

    """
    punc = str.maketrans('', '', "'")
    for row in tqdm(range(len(df))):
        df.loc[row,column] = df.loc[row,column].translate(punc)
