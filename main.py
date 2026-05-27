from analyzer import reaction_type
import customtkinter as ctk 
app = ctk.CTk()
app.title("Chemical Reaction Analyzer")
app.geometry("500x400")
title = ctk.CTkLabel(app, text="Chemical Reaction Analyzer")
title.pack(pady=20)
entry = ctk.CTkEntry(app, width=300)
entry.pack(pady=10)
result = ctk.CTkLabel(app, text="Result:")
result.pack(pady=20)
def analyze_reaction():
    reaction= entry.get()
    reaction_result = reaction_type(reaction)
    result.configure(text="result:"+ reaction_result)
button = ctk.CTkButton(
     app,
    text="Analyze",
    command=analyze_reaction)
button.pack(pady=20)    
app.mainloop()