# Définition de la longueur maximale pour les mots de passe
max_length = int(input("Quelle longueur ?     "))

# Liste des caractères d'un clavier azerty européen
keyboard_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

# Fonction récursive pour générer toutes les combinaisons de mots de passe
def generate_passwords(password, max_length):
  # Si la longueur du mot de passe atteint la limite maximale, on l'ajoute au fichier
  if len(password) == max_length:
    with open("passwords.txt", "a") as f:
      f.write(password + "\n")
    return
  
  # Sinon, on génère les mots de passe en ajoutant chacun des caractères du clavier azerty européen à la fin du mot de passe actuel
  for char in keyboard_chars:
    generate_passwords(password + char, max_length)

# Appel de la fonction pour générer les mots de passe de longueur maximale 8
generate_passwords("", max_length)
