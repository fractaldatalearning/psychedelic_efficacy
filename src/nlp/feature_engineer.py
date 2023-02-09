
def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def get_polarity(text):
    return TextBlob(text).sentiment.polarity


def analyze_sentiment(df, column):

    """Engineers subjectivity and polarity features for each string in a column.

    Args:
        df: dataframe that contains a column of strings
        column: name of column full of strings 

    Returns: a new column added to the dataframe that contains a subjectivity score between 0 and 1
        and a column that contains polarity score between -1 and 1 (negative or positive sentiment)
        associated with the text of each string. 

    """
    df['subjectivity'] = df[column].apply(get_subjectivity)
    df['polarity'] = df[column].apply(get_polarity)



   
