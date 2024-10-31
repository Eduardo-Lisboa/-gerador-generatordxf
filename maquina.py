import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import ezdxf

# Variável global para armazenar o diretório de salvamento
diretorio_salvamento = ""

# Função para criar o desenho em DXF com a furação
def criar_dxf_com_furo(peca):
    nome, quantidade, largura, altura, espessura = peca
    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()
    
    for i in range(quantidade):
        # Desenha a peça como um retângulo
        msp.add_lwpolyline([(0, 0), (largura, 0), (largura, altura), (0, altura), (0, 0)], close=True)
        
        # Adiciona o furo de 10mm de diâmetro a 50mm da largura e 20mm da altura
        x_furo = 50
        y_furo = 20
        msp.add_circle((x_furo, y_furo), radius=10/2)
        
        # Salva o arquivo DXF com o nome da peça e número do item
        caminho_arquivo = f"{diretorio_salvamento}/{nome.replace(' ', '')}{i+1}.dxf"
        doc.saveas(caminho_arquivo)
        print(f"Arquivo {caminho_arquivo} criado com sucesso.")

# Função para adicionar peça à lista
def adicionar_peca():
    nome = entry_nome.get()
    quantidade = int(entry_quantidade.get())
    largura = int(entry_largura.get())
    altura = int(entry_altura.get())
    espessura = int(entry_espessura.get())
    
    peca = (nome, quantidade, largura, altura, espessura)
    pecas.append(peca)
    atualizar_lista()
    messagebox.showinfo("Sucesso", f"Peça {nome} adicionada com sucesso!")
    
    # Limpar os campos de entrada
    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_largura.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_espessura.delete(0, tk.END)

# Função para atualizar a lista de peças na interface
def atualizar_lista():
    for item in tree.get_children():
        tree.delete(item)
    for peca in pecas:
        tree.insert("", tk.END, values=peca)

# Função para gerar arquivos DXF para todas as peças
def gerar_dxf():
    if not pecas:
        messagebox.showerror("Erro", "A lista de peças está vazia. Adicione pelo menos uma peça antes de gerar os arquivos DXF.")
        return
    
    if not diretorio_salvamento:
        messagebox.showerror("Erro", "Selecione um diretório para salvar os arquivos DXF.")
        return
    
    if messagebox.askyesno("Confirmação", "Você realmente deseja gerar os arquivos DXF?"):
        for peca in pecas:
            criar_dxf_com_furo(peca)
        pecas.clear()
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Arquivos DXF gerados com sucesso e lista de peças zerada.")
    else:
        messagebox.showinfo("Informação", "Adicione mais peças antes de gerar os arquivos DXF.")

# Função para excluir uma peça da lista
def excluir_peca():
    selected_item = tree.selection()
    if selected_item:
        item_index = tree.index(selected_item)
        del pecas[item_index]
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Peça excluída com sucesso.")
    else:
        messagebox.showerror("Erro", "Selecione uma peça para excluir.")

# Função para editar uma peça da lista
def editar_peca():
    selected_item = tree.selection()
    if selected_item:
        item_index = tree.index(selected_item)
        peca = pecas[item_index]
        
        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, peca[0])
        entry_quantidade.delete(0, tk.END)
        entry_quantidade.insert(0, peca[1])
        entry_largura.delete(0, tk.END)
        entry_largura.insert(0, peca[2])
        entry_altura.delete(0, tk.END)
        entry_altura.insert(0, peca[3])
        entry_espessura.delete(0, tk.END)
        entry_espessura.insert(0, peca[4])
        
        del pecas[item_index]
        atualizar_lista()
    else:
        messagebox.showerror("Erro", "Selecione uma peça para editar.")

# Função para selecionar o diretório de salvamento
def selecionar_diretorio():
    global diretorio_salvamento
    diretorio_salvamento = filedialog.askdirectory()
    if diretorio_salvamento:
        label_diretorio.config(text=f"Diretório de salvamento: {diretorio_salvamento}")

# Lista de peças
pecas = []

# Criação da janela principal
root = tk.Tk()
root.title("Gerador de Peças DXF")

# Estilo
style = ttk.Style()
style.configure("TLabel", padding=6)
style.configure("TButton", padding=6)

# Frame principal
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Widgets para entrada de dados
ttk.Label(mainframe, text="Nome da Peça").grid(row=0, column=0, sticky=tk.W)
entry_nome = ttk.Entry(mainframe, width=25)
entry_nome.grid(row=0, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Quantidade").grid(row=1, column=0, sticky=tk.W)
entry_quantidade = ttk.Entry(mainframe, width=25)
entry_quantidade.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Largura").grid(row=2, column=0, sticky=tk.W)
entry_largura = ttk.Entry(mainframe, width=25)
entry_largura.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Altura").grid(row=3, column=0, sticky=tk.W)
entry_altura = ttk.Entry(mainframe, width=25)
entry_altura.grid(row=3, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Espessura").grid(row=4, column=0, sticky=tk.W)
entry_espessura = ttk.Entry(mainframe, width=25)
entry_espessura.grid(row=4, column=1, sticky=(tk.W, tk.E))

# Botão para adicionar peça
btn_adicionar = ttk.Button(mainframe, text="Adicionar Peça", command=adicionar_peca)
btn_adicionar.grid(row=5, column=0, columnspan=2, pady=10)

# Botão para selecionar diretório de salvamento
btn_selecionar_diretorio = ttk.Button(mainframe, text="Selecionar Diretório", command=selecionar_diretorio)
btn_selecionar_diretorio.grid(row=6, column=0, columnspan=2, pady=10)

# Label para mostrar o diretório de salvamento selecionado
label_diretorio = ttk.Label(mainframe, text="Diretório de salvamento: Não selecionado")
label_diretorio.grid(row=7, column=0, columnspan=2, pady=10)

# Botão para gerar arquivos DXF
btn_gerar = ttk.Button(mainframe, text="Gerar DXF", command=gerar_dxf)
btn_gerar.grid(row=8, column=0, columnspan=2, pady=10)

# Treeview para mostrar a lista de peças
tree = ttk.Treeview(mainframe, columns=("Nome", "Quantidade", "Largura", "Altura", "Espessura"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Quantidade", text="Quantidade")
tree.heading("Largura", text="Largura")
tree.heading("Altura", text="Altura")
tree.heading("Espessura", text="Espessura")
tree.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Botão para excluir peça
btn_excluir = ttk.Button(mainframe, text="Excluir Peça", command=excluir_peca)
btn_excluir.grid(row=10, column=0, pady=10)

# Botão para editar peça
btn_editar = ttk.Button(mainframe, text="Editar Peça", command=editar_peca)
btn_editar.grid(row=10, column=1, pady=10)

# Configuração de espaçamento
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Inicia o loop principal da interface gráfica
root.mainloop()