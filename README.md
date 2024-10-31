# Gerador de Peças DXF

Este projeto é uma aplicação GUI em Python que permite aos usuários adicionar peças com dimensões específicas e gerar arquivos DXF para essas peças. A interface gráfica é construída usando a biblioteca `tkinter`.

## Funcionalidades

- **Selecionar Diretório de Salvamento:** Permite ao usuário selecionar o diretório onde os arquivos DXF serão salvos.
- **Adicionar Peças:** Permite ao usuário adicionar peças com nome, quantidade, largura, altura e espessura.
- **Gerar Arquivos DXF:** Gera arquivos DXF para as peças adicionadas.
- **Exibir Lista de Peças:** Exibe a lista de peças adicionadas em um widget `Treeview`.

## Descrição do Código

### Botão para Selecionar Diretório

```python
btn_selecionar_diretorio.grid(row=6, column=0, columnspan=2, pady=10)