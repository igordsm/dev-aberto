<!-- $theme: default -->

Desenvolvimento Aberto
===

![100%](capa.svg)

##### Documentação de API + testes


###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )

---
# Atividade - objetivos

Transformar o projeto DesSoft-Desafios em um projeto *profissional*

1. Documentação de usuário (aluno e professor)
2. Documentação de desenvolvimento
3. Traduções e internacionalização (datas)

---
# Atividade - objetivos

Transformar o projeto DesSoft-Desafios em um projeto *profissional*

1. Documentação de usuário (aluno e professor)
2. Documentação de desenvolvimento
	- Estrutura de projeto
	- **API**
3. Traduções e internacionalização (datas)

---
# Hoje

* Demonstração das traduções e documentações de vocês
* Documentação de API usando 
	- pydoc
	- sphinx-autodoc
* Padrões de formatação de código
	- linters
	- PEP8

---
# Documentação de API

**Objetivo**: explicar o funcionamento das funções, classes e módulos de um programa. 

* Focado em detalhes
* Documenta os argumentos esperados e em quais situações a função funciona 
* Tipicamente obtida direto do código

---
# Documentação de API

![center](api-doc.svg)

---
# Documentação de API

![2000% center](np-doc-api.png)

[ref](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html)

---
# Ferramentas

* Python:
	- pydoc, **sphinx-apidoc**
* C/C++
	- Doxygen
* Java
	- Javadoc

---
# Padrões de codificação

![300% center](porco.png)

---
# Padrões de codificação

![500% center](porco-pylint.png)

---
# Padrões de codificação

* Cada projeto tem o seu
* Algumas linguagens tem um estilo padrão
	- Python - PEP8
* Ferramentas ajudam a conferir (forçar) um estilo específico

---
# Ferramentas

* Python: pylint
* C/C++: splint, cppchecker, gcc (opções -Wall, -Wextra)
* Java: flag `-Xlint`
* Javascript: ESlint, TSlint (typescript)

#

Ajudam a manter código limpo e legível. Podem ser plugadas no seu editor/IDE favorito.


---
# Testes automatizados

**Ideia**: escrever um programa que verifica se um outro programa responde como esperado

* Definir situações a serem testadas ...
* e o resultado esperado em cada situação

---
# Testes automatizados

**Não ajudam**:

* a revelar novos bugs
* a garantir que um software é livre de bugs

**Ajudam**

* a evitar que bugs descobertos voltem
* a evitar que mudanças não intencionais quebrem código que estava funcionando.
* a documentar em quais situações o software funciona.

---
# Testes unitários

**Ideia**: dada uma função, verificar se ela devolve o valor esperado para um certo conjunto de parâmetros. 

* Testa as funções de maneira **isolada**
* **Cobertura**: porcentagem das linhas de código que é executada durante os testes de unidade.
* Serve como documentação da função

---
# Testes unitários - pytest

![140% center](pytest.png)

---

## **O quê eu preciso testar?**

# 

# 

Ninguém sabe de verdade.... 

----
# Atividade prática

Vamos finalizar nosso projeto de DesSoft hoje:

![200% center](../../skills/images/shiny-code.svg)

**Skill**: Shiny Code - documentou API do sistema e passou *linter*
**Proof**: url do fork de vocês com tudo funcionando.

Vocês deverão usar **sphinx-apidoc** e fazer a documentação usando *docstrings*.

----
# Atividade prática

Opcional: criar um conjunto de testes usando 

![100% center](../../skills/images/tested-approved.svg)

**Skill**: Testado e aprovado - criou conjunto de testes para o sistema de DesSoft
**Proof**: url do arquivo de testes no Github

---


Desenvolvimento Aberto
===

![100%](capa.svg)

##### Documentação de API + testes


###### Igor dos Santos Montagner ( [igorsm1@insper.edu.br](mailto:igorsm1@insper.edu.br) )


