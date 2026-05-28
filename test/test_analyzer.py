from analyzer import reaction_type 
def test_reaction():
    asent reaction_type("H2 + O2") == "Combustion Reaction"