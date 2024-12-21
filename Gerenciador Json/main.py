import json
import tkinter as tk
from tkinter import simpledialog, messagebox

def criar_arquivo_json():
    usuarios = [
        {"nome": "João", "idade": 25},
        {"nome": "Maria", "idade": 30}
    ]
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
    messagebox.showinfo("Sucesso", "Arquivo JSON criado com sucesso!")

def obter_entrada_usuario():
    nome = simpledialog.askstring("Input", "Digite o nome do usuário:").strip()
    while True:
        try:
            idade = int(simpledialog.askstring("Input", "Digite a idade do usuário:").strip())
            if idade < 0:
                raise ValueError
            break
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira uma idade válida e positiva.")
    return {"nome": nome, "idade": idade}

def adicionar_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        novo_usuario = obter_entrada_usuario()
        usuarios.append(novo_usuario)

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado. Crie o arquivo primeiro.")

def remover_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        nome = simpledialog.askstring("Input", "Digite o nome do usuário a ser removido:").strip()
        usuarios = [usuario for usuario in usuarios if usuario['nome'] != nome]

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado. Crie o arquivo primeiro.")

def exibir_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        lista_usuarios = "\n".join([f"Nome: {usuario['nome']}, Idade: {usuario['idade']}" for usuario in usuarios])
        messagebox.showinfo("Usuários Registrados", lista_usuarios)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado. Crie o arquivo primeiro.")

def main():
    root = tk.Tk()
    root.title("Gerenciador de Usuários JSON")

    tk.Button(root, text="Criar Arquivo JSON", command=criar_arquivo_json).pack(fill=tk.BOTH)
    tk.Button(root, text="Adicionar Usuário", command=adicionar_usuario).pack(fill=tk.BOTH)
    tk.Button(root, text="Remover Usuário", command=remover_usuario).pack(fill=tk.BOTH)
    tk.Button(root, text="Exibir Usuários", command=exibir_usuarios).pack(fill=tk.BOTH)
    tk.Button(root, text="Sair", command=root.quit).pack(fill=tk.BOTH)

    root.mainloop()

if __name__ == "__main__":
    main()
