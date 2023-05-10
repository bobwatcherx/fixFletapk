from flet import *


def main(page:Page):
	page.add(
Column([
	Text("Flet App",size=30),
	TextField(label="Name")
	])
		)

flet.app(target=main)
