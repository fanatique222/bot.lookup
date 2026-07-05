import discord 
from discord import app_commands
import sqlite3
omport os

#connexion aux DB français (création si inexistante)
conn = sqlite3.connect('french_db.db')
c = conn.cursor()

# Création des tables avec données française simulées (ajoute tes dumps 
CSV/DB ici)
c.execute('''CREATE TABLE IF NOT EXISTS 
personnes (
  id INTEGER PRIMARY KEY,
  nom TEXT,
  prenom TEXT,
  adresse TEXT,
  ville TEXT,
  code_postal TEXT,
  telephone TEXT,
  email TEXT,
  date_naissance TEXT
)''')


# Insertion de données exemples françaises (remplace par vraies DB)
data_examples = [
  ("Dupont","Jean","123 Rue de paris",
"Paris","75001","0612345678",
"jean.dupont@example.fr","1985-05-15"),
  ("Martin","Sophie","45 Avenue des 
Champs","Lyon","69001",
"0789456123",
"sophie.martin@example.fr",
"1992-11-20"),
  # Ajoute ici des milliers d'entrées de DB 
FR (INSEE,ect.)
]
c.executemany("INSERT OR IGNORE INTO 
personnes (nom,prenom,adresse,ville,
code_postal,telephone,email,
date_naissance) VALUES
(?,?,?,?,?,?,?)",data_examples)
conn.commit()

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
tree = 
app_commands.CommandTree(client)

@tree.command(name="lookup",
description="lookup nom prenom - 
Affiche infos personne")
@app_commands.describe(nom="Nom 
de famille",prenom="Prénom")
async def lookup(interaction:
discord.Interaction,nom: str, prenom: str):
  c.execute("SELECT * FROM personnes
 WHERE nom LIKE ? AND prenom ? 
LIMIT 5",(f"%{nom}%",f"%¨{prenom}%"))
  results = c.fetchall()
  if results:
     msg = "**Résultats trouvés :**\n"
     for row in results:
        msg += f"**{row[1]} {row[2]}
**\nAdresse: {row[3]},{row[5]} {row[4]}
\nTel: {row[6]}\nEmail: {row[7]}
\nNaissance: {row[8]}\n\n"
    await
interaction.response.send_message(msg)
  else:
   await
interaction.response.send_message("Auc
une info trouvée pour ce nom/prénom.")

@client.event
async def on_ready():
  await tree.sync()
  print(f"Bot lookup prêt ! Commande :/
lookup nom prenom")

client.run("TOKEN")

