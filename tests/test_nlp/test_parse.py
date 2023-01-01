
import pytest

import pandas as pd

from src.nlp.parse import remove_accented_chars, strip_most_punc, \
     strip_apostrophe


test_df = pd.DataFrame({'t_rating':[1,2,3,4,5], \
                        't_review':["I'd like some tea.", \
                                    "whére are yoü?", \
                                    "GIVE ME SOMETHING", \
                                    '-[]{}",<>./@^&*_~:;()!?#%', \
                                    "nower to be foun"]})

def test_remove_accented_chars():
    assert test_df['t_review'].apply(remove_accented_chars)[1] == \
           'where are you?'
           


def test_strip_most_punc():
    strip_most_punc(test_df, 't_review')
    assert test_df.t_review[3] == ':;()!?#%'


    
def test_strip_apostrophe():
    test_df = pd.DataFrame({'t_rating':[1,2,3,4,5], \
                        't_review':["I'd like some tea.", \
                                    "whére are yoü?", \
                                    "GIVE ME SOMETHING", \
                                    '-[]{}",<>./@^&*_~:;()!?#%', \
                                    "nower to be foun"]})

    strip_apostrophe(test_df, 't_review')
    assert test_df.t_review[0] == "Id like some tea."
    
