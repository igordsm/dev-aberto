

Neste roteiro trabalharemos no workflow padrão para contribuir com projetos hospedados
no Github (mas que também serve para projetos git em geral). Antes de começar cada aluno deverá 
localizar no github da disciplina a issue correspondente a criação de seu avatar. 

Nosso fluxo de trabalho será baseado em três grandes partes. Na primeira será criada uma 
cópia do repositório `igordsm/dev-aberto` onde faremos todas as mudanças necessárias. Na segunda enviaremos nossas modificações para o repositório original. Por último, atualizaremos nosso 
*fork* com modificações enviadas pelos colegas. 

Alguns pontos a serem destacados no fluxo de trabalho acima:

1. Mesmo que um usuário não tenha acesso ao repositório original ele pode trabalhar em sua cópia e somente quando tudo estiver pronto enviar suas modificações ao repositório original.  
1. É necessário que um desenvolvedor do projeto original "se responsabilize" pelas modificações externas aceitas. 
1. A aba *Pull requests* permite que os desenvolvedores discutam as propostas de modificações e as melhorem. Todo commit feito após a criação do PR é incluido e pode ser testado por qualquer um.

# Parte 1 - Criando uma cópia local

Descrever aqui como criar um fork e branch para cada issue.

## Criando um avatar

Para adicionar um avatar na disciplina basta editar o arquivo *players/player_list.json*. Siga o modelo do avatar já existente criado pelo professor. Imagens interessantes para seu avatar podem ser baixadas [neste site](http://untamed.wild-refuge.net/rmxpresources.php?characters). O personagem escolhido deve ser colocado na pasta *players/avatar_data*. 

O campo `uuid` deve ser preenchido com um [Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier), que pode ser gerado em Python usando o seguinte código.

```python
import uuid
print(uuid.uuid1())
```

Ao finalizar a criação do personagem execute `python update_website.py` na raiz do repositório para 
atualizar o site (localizado na pasta *docs/*). **Confira se o site gerado está funcionando corretamente antes de prosseguir!**. Seu avatar deverá estar presente na lista de participantes de sua cópia local
do site da disciplina. 

## Adicionando uma skill

Com o personagem criado podemos adicionar a skill *Penso logo existo*. Edite o arquivo *players/achievement_list.json* e adicione um novo item. O campo `proof` deve ser preenchido com a
futura url do seu avatar.

# Parte 2 - enviando as modificações



# Parte 3 - atualizando seu *fork*

Um *fork* não é atualizado quando seu repositório original correspondente receber novos commits. Para que isto ocorra é necessário realizar a sincronização *manualmente*. Isto envolve duas etapas. Na primeira, que só precisa ser feita uma vez, é adicionado um novo repositório remoto que aponta para o repositório original. Na segunda baixamos os arquivos deste repositório remoto e os incorporamos aos nossos. 

O Github tem uma excelente documentação explicando [como fazer o primeiro passo (link)](https://help.github.com/articles/configuring-a-remote-for-a-fork/) e depois [como sincronizar seu *fork* com o repositório original (link)](https://help.github.com/articles/syncing-a-fork/).