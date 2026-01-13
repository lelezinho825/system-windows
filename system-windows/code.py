import os
import shutil

class sfol:
    @staticmethod
    def cd(folder):
        os.chdir(folder)

    @staticmethod
    def md(name):
        os.mkdir(name)

    @staticmethod
    def rd(name):
        os.rmdir(name)

    @staticmethod
    def rds(name):
        shutil.rmtree(name)

    @staticmethod
    def cdp():
        os.chdir('..')

class sfil:
    @staticmethod
    def create(name):
        open(name, 'w').close()

    @staticmethod
    def cecho(content, name):
        with open(name, 'w', encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def delete(name):
        os.remove(name)

    @staticmethod
    def ren(name, newname):
        os.rename(name, newname)

class ncm:
    @staticmethod
    def infodir():
        for item in os.listdir():
            print(item)

    @staticmethod
    def startf(name):
        os.startfile(name)

    @staticmethod
    def move(name, folder):
        shutil.move(name, folder)

    @staticmethod
    def clear():
        os.system('cls')

    @staticmethod
    def help():
        helpers = [
            'SFOL:',
            'sfol.cd = Displays the folder name or changes the current folder.',
            'sfol.md = Create a folder.',
            'sfol.rd = Remove (delete) a folder.',
            'sfol.cdd = Move the path to the disk.',
            'sfol.cdp = Move to the previous folder.',
            'SFIL:',
            'sfil.create = Create a file',
            'sfil.cecho = Creates a file with content inside.',
            'sfil.copy = Copies one or more files to another location.',
            'sfil.delete = Delete one or more files.',
            'sfil.ren = Renames one or more files.',
            'NCM:',
            'ncm.infodir = Displays a list of files and subdirectories within a directory.',
            'ncm.starf = Execute a file.',
            'ncm.move = Move a file or folder.',
            'ncm.content = Displays the contents of one or more text files.',
            'ncm.clear = Clear the screen.',
            'ncm.toswitchoff = Turn off the computer.',
            'ncm.restart = Restart your computer'
        ]

        for line in helpers:
            print(f'{line} \n')
