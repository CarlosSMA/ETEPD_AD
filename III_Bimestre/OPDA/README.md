# Observatório de Projetos em Dados Abertos
## Análise de banco de dados utilizados em consultórios de dentistas

### Objetivos do projeto
- A partir de dados abertos, analisar como sistemas em produção em consultórios são projetados
- Utilizar o conjunto de tecnologias da disciplina para um projeto único
	- Python
	- Docker (containers)
	- Banco de dados SQL (Postgres)

### Como executar
1. [Instale o docker em sua máquina](https://docs.docker.com/engine/install/)
2. [Instale a imagem do postgress](https://hub.docker.com/_/postgres)
	- `docker pull postgres`
3. Crie um container a partir da imagem
	- `docker run -e POSTGRES\_PASSWORD=1234 -d --name=database -p 5432:5432 postgres`
4. Execute o container
	- `docker start database`
	- `docker run -it bash database` (em outro terminal/cmd)
5. Clone este repositório em sua máquina local
	- `git clone https://github.com/CarlosSMA/ETEPD_AD`
6. Crie um ambiente virtual python
	- `python -m pip install --upgrade pip`
	- `python -m venv venv`
	- `python main.py`
7. Acesse o container em outro terminal/cmd
	- `docker run -it bash database`
8. Insira os seguintes comandos
	- `su - postgres`
	- `psql`
	- `\l`
