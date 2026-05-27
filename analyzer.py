def reaction_type(reaction):
    if "O2" in reaction:
        return "Combustion Reaction"
    else: 
        return "Unknown Reaction"