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



# Pick up here with testing

def strip_non_emoji_emoji_symbol(df, column):

    """Deletes the symbols :;() where they appear next to letters.
        Replaces these symbols with a space: ' '. Leaves them anytime they don't appear adjacent to letters.

    Args: 
        df = dataframe with the strings to be stripped
        column: name of a column from the dataframe where strings are that should be stripped
      

    Returns: same string in the same position within the df, with ;:() removed in the fashion described above.

    """

    import re
    chars_to_remove = ['(', ')', ':', ';']
    
    # Isolate 1 narrative at a time 
    for row in tqdm(range(len(df))):
        string_to_strip = df.loc[row,column]
        # Match the ( where it appears before or after a number. 
        parenth_open_matches = re.findall('\([A-Za-z]', string_to_strip) + re.findall(
            '[A-Za-z]\(', string_to_strip)
        # Match remaining symbols
        parenth_close_matches = re.findall('\)[A-Za-z]', string_to_strip) + re.findall(
            '[A-Za-z]\)', string_to_strip)
        colon_matches = re.findall(':[A-Za-z]', string_to_strip) + re.findall(
            '[A-Za-z]:', string_to_strip)
        semicolon_matches = re.findall(';[A-Za-z]', string_to_strip) + re.findall(
            '[A-Za-z];', string_to_strip)
        # combine all lists to capture all matched strings where any symbols should be replaced
        all_matches = list(parenth_open_matches + parenth_close_matches + colon_matches + 
                           semicolon_matches)
        # Now replace just the symbols, not the numbers, in these matched strings
        for match in all_matches: 
            for char in chars_to_remove:
                string_to_strip = string_to_strip.replace(match, match.replace(char, ''))
        df.loc[row,column] = string_to_strip




def strip_emoji_like_if_spaces(df, column):

    """Deletes the symbols :;() where they appear surrounted entirely by spaces i.e. ' ( '.
        Replaces these symbols with nothing: ''. Leaves them anytime they don't appear adjacent to numbers.

    Args: 
        df = dataframe with the strings to be stripped
        column: name of a column from the dataframe where strings are that should be stripped
      

    Returns: same string in the same position within the df, with ;:() removed in the fashion described above.

    """

    remove_if_spaces = [' ( ', ' ) ', ' : ', ' ; ']
    for char in remove_if_spaces:
    # Replace each character surrounded by spaces with just a single space
        df[column] = df[column].str.replace(char, '', regex=False)




def strip_emoji_sym_adjacent_number(df, column):

    """Deletes the symbols :;() where they appear next to numbers.
        Replaces these symbols with nothing: ''. Leaves them anytime they don't appear adjacent to numbers.

    Args: 
        df = dataframe with the strings to be stripped
        column: name of a column from the dataframe where strings are that should be stripped
      

    Returns: same string in the same position within the df, with ;:() removed in the fashion described above.

    """

    import re
    chars_to_remove = ['(', ')', ':', ';']
    
    # Isolate 1 narrative at a time 
    for row in tqdm(range(len(df))):
        string_to_strip = df.loc[row,column]
        # Match the ( where it appears before or after a number. 
        parenth_open_matches = re.findall('\([0-9]', string_to_strip) + re.findall(
            '[0-9]\(', string_to_strip)
        # Match remaining symbols
        parenth_close_matches = re.findall('\)[0-9]', string_to_strip) + re.findall(
            '[0-9]\)', string_to_strip)
        colon_matches = re.findall(':[0-9]', string_to_strip) + re.findall(
            '[0-9]:', string_to_strip)
        semicolon_matches = re.findall(';[0-9]', string_to_strip) + re.findall(
            '[0-9];', string_to_strip)
        # combine all lists to capture all matched strings where any symbols should be replaced
        all_matches = list(parenth_open_matches + parenth_close_matches + colon_matches + 
                           semicolon_matches)
        # Now replace just the symbols, not the numbers, in these matched strings
        for match in all_matches: 
            for char in chars_to_remove:
                string_to_strip = string_to_strip.replace(match, match.replace(char, ''))
        df.loc[row,column] = string_to_strip




