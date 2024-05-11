# projeto_alura
Repositório especial para envio de projeto(s) para a premiação da Imersão IA [**Alura** &amp; **Google**]

# Pacotes utilizados neste projeto
+ google.generativeai {Este pacote oferece acesso à suíte de modelos generativos de IA do Google. Permite aos desenvolvedores integrar facilmente modelos de linguagem grandes (LLMs) em suas aplicações};
+ google.colab (userdata) {Dentro deste contexto se refere à capacidade de acessar e manipular dados do usuário dentro de um notebook Colab.
Isso pode incluir carregar arquivos, acessar variáveis de ambiente, armazenar dados persistentes e interagir com APIs.}
+ textwrap {Oferece funções para formatar e manipular strings de texto}
+ IPython.display (display e Markdown) {O display permite renderizar uma variedade de objetos em notebooks Jupyter, incluindo texto, HTML, imagens, vídeos e widgets interativos. Já o Markdown pode formatar texto usando a linguagem Markdown dentro de notebooks Jupyter}
+ requests {Este pacote oferece uma maneira elegante e intuitiva de interagir com a web em Python}
+ bs4 (BeautifulSoup) {Permite analisar documentos HTML e XML, navegar pela estrutura do documento e extrair informações específicas}

**OBS**: Essas e outras bibliotecas você pode acessar a documentação no [Pypi](https://pypi.org/), um repositório de software para a linguagem de programação Python. O PyPI ajuda você a encontrar e instalar softwares desenvolvidos e compartilhados pela comunidade do Python.

# Técnica utilizada no prompt do Gemini para este projeto

*Few-shot Chain-of-Thought Prompting* (Um raciocínio passo a passo com alguns exemplos). A ideia era produzir um prompt bem detalhado, a fim de extrair uma ótima resposta do Gemini

# Instalação da Biblioteca do Google para IA e utilização da API Key

```bash
!pip install -q -U google-generativeai
```
**OBS**: o recurso '-q' permite uma instalação silenciosa, ou seja, sem aquele output imenso, enquanto o '-U' serve para obter a versão mais atualizada do pacote.

```python
import google.generativeai as genai

from google.colab import userdata
chave_secreta = userdata.get('COLOQUE_A_SUA_API_KEY')

genai.configure(api_key=chave_secreta)
```
Você pode obter a API Key acessando o [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat) e clicando no botão **Get API key**

<img width="959" alt="Captura de tela 2024-05-11 163007" src="https://github.com/marioluciofjr/projeto_alura/assets/105465306/09c7fa16-06af-4af4-b2b6-fdd7d2ad8a5e">

---------------------------------------------------------------------------------

## PresenteIA
Você não quer mais quebrar a cabeça na hora de escolher presentes? 🤯🎁
Seus problemas acabaram! 

Com o PresenteIA você terá um guru de presentes e obter sugestões de termos de busca para procurar no e-commerce, bem como dicas financeiras a partir do 
conceito de finanças comportamentais de Daniel Kahneman, Prêmio Nobel de Economia.

---------------------------------------------------------------------------------

### Dicas úteis para bom uso do código

![Screenshot - 2024-05-10T092530 435](https://github.com/marioluciofjr/projeto_alura/assets/105465306/edf02446-4835-4e83-b11c-80deb8500a0d)

Eu utilizei a dica do Fabrício Carraro para colocar a API Key do Google utilizando o painel Secrets do Google Colab. 
---> chave_secreta = userdata.get('AQUI VOCÊ BATIZA SUA CHAVE SECRETA') e coloca em *Nome* no Secrets, que você acessa pelo ícone de chave. 
Em *Valor* vai a sua API Key. Aí é só habilitar em *Acesso ao notebook*.

---------------------------------------------------------------------------------

![Screenshot - 2024-05-10T094541 430](https://github.com/marioluciofjr/projeto_alura/assets/105465306/d3205dce-5e5b-4d2f-b103-3cd38d88a284)

Esses inputs são importantíssimos para uma boa resposta do Gemini, portanto, não precisa poupar palavras. 

+ **status_de_relacionamento** = O que a pessoa é para você? (mãe, pai, namorada(o), ficante, colega, amiga(o), desconhecida(o) etc.)
+ **características** = Quais são as principais caraterísticas físicas e/ou psicológicas da pessoa que você quer presentear?
+ **lazer** = Como essa pessoa se diverte?
+ **ocasião** = Que data comemorativa ou evento merece esse presente?
+ **dinheiro_disponível** = Quanto você pretende gastar com o presente?

---------------------------------------------------------------------------------

![Screenshot - 2024-05-10T101941 358](https://github.com/marioluciofjr/projeto_alura/assets/105465306/b43204db-ebf4-4652-8b86-61dc3dba7bca)

A primeira parte do código é a interação com o Gemini, que fornecerá três tipos de termos de busca para você pesquisar. 
A ideia é você escolher uma das sugestões do Gemini e pesquisar no código que busca as 10 melhores opções com essa palavra-chave no Mercado Livre.

Escolhi o Mercado Livre como e-commerce referência, pois confio na plataforma.

---------------------------------------------------------------------------------

### Como utilizar o código?

Clica aqui para acessar a pasta com o código em Python ---> https://github.com/marioluciofjr/projeto_alura/blob/main/PresenteIA.ipynb

![Screenshot - 2024-05-11T150800 461](https://github.com/marioluciofjr/projeto_alura/assets/105465306/967d6491-1722-4063-91d4-a0da2bd8befe)

Depois é só clicar no botão **Open in Colab**

---------------------------------------------------------------------------------

#### Desenvolvedor 
Mário Lúcio

##### 🔗 [Site](https://prazocerto.me) | [LinkedIn](https://linkedin.com/in/marioluciofjr)
