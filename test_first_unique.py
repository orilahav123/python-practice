from first_unique import first_unique

def test_first_unique():
    assert first_unique(["חיפה", "אילת", "חיפה", "תל אביב"]) == "אילת"
    assert first_unique(["d","d","d"]) == None
    assert first_unique([]) == None
    assert first_unique(["חיפה", "חיפה", "אילת", "אילת"]) ==None
    assert first_unique(["sam","sam","mor","mor","mor","dor"]) == "dor"
    assert first_unique(["ג", "א", "א"]) == "ג"
    assert first_unique(["חיפה"]) == "חיפה" 