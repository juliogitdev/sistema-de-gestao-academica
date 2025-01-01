
def mudar_tela(root, tela_nova):
    # Limpa todos os widgets da tela atual
    for widget in root.winfo_children():
        widget.grid_forget()
    
    # Exibe a nova tela
    tela_nova(root)

def limpar_root(root):
        for widget in root.winfo_children():
            widget.destroy()
        for i in range(root.grid_size()[0]):  # Limpa configurações de coluna
            root.grid_columnconfigure(i, weight=0)
        for i in range(root.grid_size()[1]):  # Limpa configurações de linha
            root.grid_rowconfigure(i, weight=0)
        
        return root