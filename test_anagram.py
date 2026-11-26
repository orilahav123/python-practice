import pytest
from anagram import is_anagram

def test_anagram_true():
    assert is_anagram("mor","rom") == True
    
def test_anagram_false():
    assert is_anagram("noam","ori") == False
    
def test_anagram_edge_case():
    assert is_anagram("Mor","rom") == True
 
def test_anagram_empty_strings():
    with pytest.raises(ValueError):
        is_anagram("","")  
    
def test_anagram_one_empty_string():
    with pytest.raises(ValueError):
        is_anagram("", "a")