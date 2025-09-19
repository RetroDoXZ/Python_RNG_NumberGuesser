
import tkinter as tk #lager GUI (tkinter)
import random

# --- Spillets logikk og tilstand ---
secret = random.randint(1, 100) #tilfeldig tall 1-100
attempts = 0 #antall forsøk
guesses = [] #lagrer gjetninger og svar
try_again_btn = None #prøv-igjen knapp, starter som None

def check_guess(): #sjekker gjetningen sjekk, oppdater, logg osv.
	global attempts
	# prøver å hente tall fra entry. Merk: hvis bruker skriver noe rart krasjer det – antar heltall her
	guess = int(entry.get()) #henter tall fra entry og gjør det til int
	attempts += 1 #øker antall forsøk
	# sammenligner gjetning med hemmelig tall
	if guess < secret: #for lavt
		feedback = "For lavt!" #tilbakemelding: for lavt
	elif guess > secret: #for høyt
		feedback = "For høyt!" #tilbakemelding: for høyt
	# Merk: hvis man skriver inn tekst eller komma-tall krasjer programmet
	else:
		# når riktig: lager en beskjed og viser knapp for ny runde
		feedback = f"Korrekt! Du gjettet det på {attempts} forsøk." #riktig
		show_try_again() #viser «prøv igjen»-knappen
	# legger til i lista som vises i loggen
	guesses.append(f"{guess}: {feedback}") #oppdaterer liste
	result.set(feedback) #oppdaterer visning
	log.set('\n'.join(guesses)) #viser alle gjetninger
	entry.delete(0, tk.END) #tømmer entry

def show_try_again(): #viser knapp for ny runde
	global try_again_btn
	# hvis knappen ikke finnes: lag den og koble til reset_game
	if try_again_btn is None:
		try_again_btn = tk.Button(root, text="Prøv igjen", font=("Segoe UI", 11, "bold"), bg="#00adb5", fg="#222831", activebackground="#393e46", activeforeground="#00adb5", relief="flat", padx=10, pady=5, command=reset_game) #lager knappe stil og farge
		try_again_btn.pack(pady=5) #plasserer knappen
	else:
		try_again_btn.pack(pady=5) #viser knapp

def reset_game(): #starter spillet på nytt
	global secret, attempts, guesses
	# Genererer nytt tall kan være samme som før hvis uheldig
	secret = random.randint(1, 100) #nytt tall
	attempts = 0 #nullstiller forsøk
	guesses = [] #tømmer listen
	# nullstiller visningsvariabler
	result.set("") #tømmer resultat
	log.set("") #tømmer logg
	entry.delete(0, tk.END) #tømmer entry-felt
	# skjuler «prøv igjen»-knappen
	if try_again_btn:
		try_again_btn.pack_forget() #skjuler knapp
	# ekstra kommentar med skrivefeil og forklaring: «reset_game skal sette alt tibake til start, inklusiv at `attempts` blir 0 og at lista `guesses` blir tom. sjekk at ingen referanser står igjen som kan føre til gamle data.»

def on_enter(event=None): #binder Enter til sjekk
	check_guess()


# --- GUI oppsett ---
if __name__ == "__main__":
	root = tk.Tk() #hovedvindu
	root.title("Gjett Tallet") #tittel
	root.state('zoomed') #starter i fullskjerm
	root.configure(bg="#222831") #bakgrunnsfarge

	entry = tk.Entry(root, width=30, font=("Segoe UI", 12), bg="#393e46", fg="#eeeeee", insertbackground="#eeeeee", relief="flat") #input-felt
	entry.pack(pady=(20, 10)) #plassering

	btn = tk.Button(root, text="Gjett", command=check_guess, font=("Segoe UI", 11, "bold"), bg="#00adb5", fg="#222831", activebackground="#393e46", activeforeground="#00adb5", relief="flat", padx=10, pady=5) #gjett-knapp
	btn.pack(pady=5) #plassering

	result = tk.StringVar() #lagrer resultat
	label = tk.Label(root, textvariable=result, font=("Segoe UI", 13, "bold"), bg="#222831", fg="#00adb5") #label for resultat
	label.pack(pady=10) #plassering

	log = tk.StringVar() #lagrer logg
	log_label = tk.Label(root, textvariable=log, justify="left", font=("Segoe UI", 10), bg="#222831", fg="#eeeeee") #label for logg
	log_label.pack(pady=(0, 10)) #plassering

	entry.bind('<Return>', on_enter) #definerer "keybind" for Enter-tasten
	root.mainloop() #starter GUI