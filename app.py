import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///cadastro_de_produto.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    page.title = 'App - Cadastro de Produtos'
    lista_produtos = ft.ListView()

    def cadastrar(e):
        try:
            if not produto.value or not preco.value:
                raise ValueError("Os campos não podem estar vazios.")
            float(preco.value) 
            
            novo_produto = Produto(
            titulo=produto.value,
            preco=float(preco.value)
            )
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(ft.Container(
                    ft.Text(produto.value + f' - R$ {preco.value}'),
                    bgcolor=ft.Colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                ))
            txt_erro.visible = False
            txt_acerto.visible = True

            produto.value = ''
            preco.value = 0
        except:
            txt_erro.visible = True
            txt_acerto.visible = False 

        page.update()
        print(f'Produto {novo_produto.titulo} cadastrado com sucesso!')

    txt_erro = ft.Container(ft.Text('Erro ao salvar o produto!'), bgcolor=ft.Colors.RED, padding=10, visible=False, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Produto salvo com sucesso!'), bgcolor=ft.Colors.GREEN, padding=10, visible=False, alignment=ft.alignment.center)

    txt_titulo = ft.Text('Cadastrar novo produto') 
    produto = ft.TextField(label='Digite o titulo do  produto...', text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto: ')
    preco = ft.TextField(value=0, label='Digite o preço do produto...', text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_acerto,
        txt_erro,
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(f'{p.titulo} - R$ {p.preco:.2f}'),
                bgcolor=ft.Colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )

    page.add(
        lista_produtos,
    )

ft.app(target=main)
