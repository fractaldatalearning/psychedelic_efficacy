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
      column: name of a column from the dataframe where strings are that should be stripped

    Returns: same string in the same position within the df, with listed characters removed and replaced with a space

    """
    punc = str.maketrans('', '', '-[]{}",<>./@^&*_~')
    for row in tqdm(range(len(df))):
        df.loc[row,column] = df.loc[row,column].translate(punc)



def strip_apostrophe(df, column):

    """Deletes apostrophes wherever they appear in strings in a dataframe column. 

    Args: 
      df: name of dataframe
      column: name of a column from the dataframe where strings are that should be stripped

    Returns: same string in the same position within the df, with apostrophes removed

    """
    punc = str.maketrans('', '', "'")
    for row in tqdm(range(len(df))):
        df.loc[row,column] = df.loc[row,column].translate(punc)



# This function isn't passing its test, and it's wonky toward the bottom. It does get the job jone, but try to
# Improve the if statement to be more streamlined, universally applicable. 
def strip_non_emoji_emoji_symbol(df, column):

    """Deletes the symbols :;() where they appear next to letters.
        Replaces these symbols with a space ' '. Leaves them anytime they don't appear adjacent to letters.

    Args: 
      df: name of dataframe
      column: name of a column from the dataframe where strings are that should be stripped

    Returns: same string in the same position within the df, with ;:() removed in the fashion described above.

    """

    # Isolate 1 narrative at a time 
    import re
    for row in tqdm(range(len(df))):
        string_to_strip = df.loc[row,column]
        
        # Find each ) that appears next to letters, not other symbols.
        closing_parentheses = [m.end() for m in re.finditer('[a-zA-z]\)', string_to_strip)]
        # That's not capturing the correct character. Fix this.
        clos_parenth_indices = [n - 1 for n in closing_parentheses]
        # Find each ( 
        opening_parentheses = [m.start() for m in re.finditer('\([a-zA-z]', string_to_strip)]
        # Find each : 
        colon_after_word = [m.end() for m in re.finditer('[a-zA-z]\:', string_to_strip)]
        colon_after_indices = [n - 1 for n in colon_after_word]
        colon_before_word = [m.start() for m in re.finditer('\:[a-zA-z]', string_to_strip)]
        # find each ; 
        semicolon_after_word = [m.end() for m in re.finditer('[a-zA-z]\;', string_to_strip)]
        semicolon_after_indices = [n - 1 for n in semicolon_after_word]
        semicolon_before_word = [m.start() for m in re.finditer('\;[a-zA-z]', string_to_strip)]

        # Combine lsits of indices in order to replace all characters 
        indices_to_remove = clos_parenth_indices + opening_parentheses + colon_after_indices \
        + colon_before_word + semicolon_after_indices + semicolon_before_word
        
        # Replace target characters in the string to strip with just a space ' '
        # Use a space ' ' instead of nothing '' in case of something like:this 
        temp = list(string_to_strip)
        for index in indices_to_remove:
            temp[index] = ' '
            result = ''.join(temp)
            new_string = str(result)
        # If there were no changes to be made, new_string stays the same as it was for the row before
        # Or even several rows back. Make sure reviews don't get over-written with previous rows' reviews
        if row>0 and new_string == df.loc[row-1,column]:
            df.loc[row,column] = df.loc[row,column]
        elif row>1 and new_string == df.loc[row-2,column]:
            df.loc[row,column] = df.loc[row,column]
        elif row>2 and new_string == df.loc[row-3,column]:
            df.loc[row,column] = df.loc[row,column]
        elif row>3 and new_string == df.loc[row-4,column]:
            df.loc[row,column] = df.loc[row,column]
        elif row>4 and new_string == df.loc[row-5,column]:
            df.loc[row,column] = df.loc[row,column]
        elif row>5 and new_string == df.loc[row-6,column]:
            df.loc[row,column] = df.loc[row,column]
        elif row>6 and new_string == df.loc[row-7,column]:
            df.loc[row,column] = df.loc[row,column]
        elif row>7 and new_string == df.loc[row-8,column]:
            df.loc[row,column] = df.loc[row,column]
        # As long as it's not getting overwritten incorectly, replace review with new, stripped string
        else: df.loc[row,column] = new_string
