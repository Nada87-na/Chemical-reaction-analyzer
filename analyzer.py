def reaction_type(reaction):
    reaction = reaction.lower()
    if "O2" in reaction:
        return "Combustion Reaction"
    elif "na" in reaction and "cl" in reaction:
        return "Synthesis Reaction"    
    elif "hcl" in reaction:
        return "Acid Reaction"    
    else:
        return "Unknown Reaction"    