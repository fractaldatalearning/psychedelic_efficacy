import unicodedata # for function remove_accented_chars

def remove_accented_chars(text):
    """Turns accented characters i.e. é, ä into unaccented characters ie e, a, in a string

    Args: 
      text: string containing any characters

    Returns: same string, with any accented characters replaced

    """
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

