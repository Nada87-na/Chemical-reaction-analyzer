import customtkinter as ctk
from analyzer import reaction_type

 
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  


app = ctk.CTk()
app.title("Chemical Reaction Analyzer")
app.geometry("500x400")


title = ctk.CTkLabel(app, text="Chemical Reaction Analyzer", font=("Helvetica", 20, "bold"))
title.pack(pady=30)

 
entry = ctk.CTkEntry(app, width=350, placeholder_text="Enter chemical reaction (e.g., H2 + O2 -> H2O)")
entry.pack(pady=15)

 
def analyze_reaction():
    reaction = entry.get()
    reaction_result = reaction_type(reaction)
    result.configure(text=f"Result: {reaction_result}")


button = ctk.CTkButton(app, text="Analyze", font=("Helvetica", 14, "bold"), command=analyze_reaction)
button.pack(pady=20)


result = ctk.CTkLabel(app, text="Result: ", font=("Helvetica", 16))
result.pack(pady=20)


app.mainloop()