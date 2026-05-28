import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer import reaction_type 
def test_reaction():
    assert reaction_type("H2 + O2") == "Combustion Reaction"
    if __name__ ==" __main__":
        test_reaction()
        print(" All tests passed successfully!")