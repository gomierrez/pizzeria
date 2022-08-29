help:
	@echo "make install: instalar el ambiente de ejecución"
	@echo "make install-local: instalar el ambiente de desarrollo"
	@echo "make shell: referenciar el ambiente de desarrollo dentro de la consola"

install:
	pipenv install

install-local:
	pipenv install --dev

shell:
	pipenv shell