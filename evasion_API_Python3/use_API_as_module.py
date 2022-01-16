from evasion import ManageVerbose, channel_to_command, send_cmd
BOX = "192.168.0.15"
PORT = 5900


def main():
    while True:
        try:
            cmd = input("Entrer un numéro de chaîne : ")
        except Exception:
            exit(0)

        try:
            ch = int(cmd)
            # On fait "taire" les fonctions exécutées
            with ManageVerbose(verbose=False):
                # On génère une liste de commandes
                cmd_ls = channel_to_command(ch)
                print(cmd_ls)
                # On envoie la liste de commandes
                # et on récupère le succès de l'envoie
                r, _ = send_cmd(BOX, PORT, cmd_ls, 2)
            print("Envoie réussi" if r else "Envoie échoué")
        except Exception:
            raise NameError('Le numéro de chaîne doit-être un entier')


if __name__ == "__main__":
    main()
