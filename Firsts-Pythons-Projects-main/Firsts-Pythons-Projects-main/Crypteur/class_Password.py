import string
CARACTERE_min = list(string.ascii_lowercase)
CARACTERE_maj = list(string.ascii_uppercase)
CARACTERE_spec = ["&", "é", '"', "'", "(", "-", "è", "_", "ç", "à", ")", "=", "%", "!", "@", "?", "/", "$", "€", "#", "+", " "]
NOMBRES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
general = (CARACTERE_maj + CARACTERE_min + NOMBRES + CARACTERE_spec)

class Password:

    def __init__(self, password, key1, key2, key3):
        self.password = password
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3

    def crypt(self, password, key1, key2, key3):
        decomp_mdp = []
        for i in password:
            decomp_mdp.append(i)

        final = []
        for l in (decomp_mdp):
            for i in range(len(general)):
                if general[i] == l:
                    i = ((i-key1)+key2)-key3
                    if i > len(general):
                        i = i -1 - len(general)
                    if i < 0:
                        i = len(general) - (i*(-1))
                    final.append(general[i])

        password = ""
        for i in(final):
            password += i 
        return password
    
    def un_crypt(self, password, key1, key2, key3):
        decomp_mdp = []
        for i in password:
            decomp_mdp.append(i)
        
        final = []
        for l in (decomp_mdp):
            for i in range(len(general)):
                if general[i] == l:
                    i = ((i+key3)-key2)+key1
                    if i > len(general):
                        i = i - len(general)
                    if i < 0:
                        i = len(general) - (i*(-1))
                    final.append(general[i])
        
        password = ""
        for i in(final):
            password += i 
        return password


    

