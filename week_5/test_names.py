import pytest
from names import make_full_name, extract_family_name, extract_given_name

def test_make_full_name():
  assert make_full_name("Sally", "Brown") == "Brown; Sally"
  assert make_full_name("John", "Doe") == "Doe; John"
  assert make_full_name("Martha", "Washington") == "Washington; Martha"
  
def test_extract_family_name():
  assert extract_family_name("Brown; Sally") == "Brown"
  assert extract_family_name("Doe; John") == "Doe"
  assert extract_family_name("Washington; Martha") == "Washington"
  
def test_extract_given_name():
  assert extract_given_name("Brown; Sally") == "Sally"
  assert extract_given_name("Doe; John") == "John"
  assert extract_given_name("Washington; Martha") == "Martha"
  
pytest.main(["-v", "--tb=line", "-rN", __file__])