install -q -U google-generativeai

import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# Função para pesquisar no Mercado Livre
def pesquisar_mercado_livre(termo_busca, filtros=None):
    url_base = "https://lista.mercadolivre.com.br/"
    url_pesquisa = url_base + termo_busca

    if filtros:
        for chave, valor in filtros.items():
            url_pesquisa += f"&{chave}={valor}"

    resposta = requests.get(url_pesquisa)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, "html.parser")
        resultados = soup.find_all("li", class_="ui-search-layout__item")

        produtos = []
        for resultado in resultados[:10]:
            titulo = resultado.find("h2", class_="ui-search-item__title").text.strip()
            link = resultado.find("a", class_="ui-search-link")["href"]
            produtos.append({"titulo": titulo, "link": link})

        return produtos
    else:
        st.error("Erro ao fazer a requisição. Código de status:", resposta.status_code)
        return []

# --- Interface Streamlit ---

st.title("🎁 PresenteIA")

# API Key
api_key = st.text_input("Insira sua API Key do Google Gemini:", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # --- Informações do Presenteado ---
    st.header("Detalhes do Presenteado")

    status_de_relacionamento = st.selectbox("Status de Relacionamento:", 
                                                ["Mãe", "Pai", "Namorada(o)", "Ficante", "Colega", "Amiga(o)", "Desconhecida(o)", "Outro"])        
    características = st.text_area("Características (opcional):")
    lazer = st.text_area("Lazer (opcional):")
    ocasião = st.text_input("Ocasião:")
    dinheiro_disponível = st.number_input("Orçamento (R$):", min_value=0.0, value=100.0, step=10.0)

    # --- Geração de Sugestões ---
    if st.button("Gerar Sugestões"):
        if not all([status_de_relacionamento, ocasião, dinheiro_disponível]):
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            with st.spinner("Gerando sugestões..."):
                # --- Prompt para o Gemini ---
                prompt = f"""{status_de_relacionamento} significa o que a pessoa é para mim.
                {características} significam um conjunto de características físicas e psicológicas que compreendo dessa pessoa.
                {lazer} é como eu enxergo que essa pessoa se diverte nas horas que não está trabalhando, estudando ou se ocupando.
                {ocasião} é a data em si que merece esse presente especial.
                {dinheiro_disponível} tem a ver com a disposição que tenho de orçamento para comprar esse presente.

                Termo de busca é uma palavra-chave específica e bem curta (no máximo 20 caracteres) para utilizar na barra de pesquisa de um site de e-commerce como o Mercado Livre.
                Exemplos de termos de busca excelentes: 'Kit churrasco gourmet', 'livro de ficção', 'panela elétrica', 'fone de ouvido sem fio' etc.

                A partir do contexto acima, siga os seguintes passos:

                1. Analise os dados informados como status de relacionamento, características, lazer e ocasião.
                2. Faça uma lista de 3 termos de busca diferentes para e-commerce que combinem o máximo possível com os detalhes informados anteriormente.
                3. Os termos de busca estarão formatados com título H2.
                4. Uma breve descrição de 2 ou 3 linhas acompanhará os termos de busca, a fim de contextualizar sua indicação e mostrar os benefícios daquele presente.
                5. Ao final, dê 2 dicas financeiras a partir do valor informado em dinheiro disponível. Leve em consideração os conceitos das finanças comportamentais de Daniel Kahneman.
                6. O título "Dicas Financeiras" estará no formato H3

                REGRAS

                1. Criatividade é muito bem-vinda, mas lembre-se que os termos de busca precisam fazer sentido para pesquisar em um e-commerce. Fornecer algo como
                "café colhido com carinho na Colômbia" não faz muito sentido numa busca. Opte por termos de busca práticos e diretos como "notebook com processador intel core i7", que seria
                uma recomendação boa para pessoas que precisam utilizar bastante o computador para trabalho/estudo.

                2. As dicas financeiras precisam ser conselhos bem-humorados, mas sem esquecer da importância que a pessoa tem para mim e que relatei tanto no status de relacionamento quanto nas características.

                3. Se o campo de características e/ou lazer estiver vazio ou com algo genérico como "Não sei". Analise essa resposta como uma indecisão. Nesse caso e somente neste caso, acrescente
                dicas para que eu entenda mais sobre a pessoa relatada no status de relacionamento.

                4. Numa escala de pesos de resposta que vai da mais importante a menos importante: 1º ocasião / 2º sataus / 3º características / 4º lazer

                EXEMPLOS DE COMO DEVE VIR SUA RESPOSTA

                Termo de busca 1: 'Kit churrasco gourmet'

                Descrição: Um kit completo com tudo que a pessoa precisa para preparar um churrasco inesquecível,
                incluindo grelha portátil, utensílios de qualidade, temperos especiais e até mesmo um livro de receitas com cortes e
                técnicas diferenciadas. Ideal para quem ama cozinhar ao ar livre e reunir amigos e familiares.

                Termo de busca 2: 'Camisa nova do Corinthians'

                Descrição: A camisa do Corinthians é mais do que um simples item de vestuário, é um símbolo de paixão, orgulho e tradição para milhões de torcedores apaixonados.
                Se você quer presentear alguém que vibra com o Timão, essa é uma escolha certeira que certamente vai emocionar e agradar!

                Termo de busca 3: 'panela elétrica'

                Descrição: Ideal para quem busca praticidade no dia a dia. A maioria dos modelos possui revestimento antiaderente, facilitando a limpeza após o uso.
                Com sistema de desligamento automático, a panela elétrica evita acidentes e garante maior segurança durante o uso. A pessoa que você vai presentear vai simplesmente amar.

                Dica financeira 1: Nossa mente adora atalhos. O primeiro preço que vemos se torna uma 'âncora' para avaliar o que vem depois.
                Então, antes de sair gastando seus 200 na primeira loja, pesquise! Compare preços online, visite diferentes lugares, explore opções.
                Você pode descobrir que aquele item "imperdível" está muito mais barato em outro lugar, ou até achar algo ainda melhor pelo mesmo valor.
                Lembre-se, sua âncora é 200, não o primeiro preço que encontrar!

                Dica financeira 2: Digamos que você já gastou 150 em um presente, mas não está totalmente convencido.
                A falácia dos custos irrecuperáveis nos faz querer insistir em algo só porque já investimos tempo, dinheiro ou esforço.
                Não caia nessa! Se o presente não está ideal, seja honesto consigo mesmo. Melhor trocar ou buscar outra opção do que ficar com algo que não vai agradar,
                mesmo que isso signifique "perder" os 150. Pense que está investindo na felicidade da pessoa (e na sua tranquilidade)!

                ---------------------------

                Termo de busca 1: 'Cafeteira italiana'
                Descrição: Um presente clássico e elegante para os amantes de café. A cafeteira italiana, também conhecida como Moka,
                produz um café encorpado e saboroso, perfeito para começar o dia ou para um momento de relaxamento.
                Escolha um modelo que combine com a personalidade da pessoa que você vai presentear e prepare-se para arrancar suspiros de felicidade.

                Termo de busca 2: 'Kindle Paperwhite'
                Descrição: Para os amantes da leitura, o Kindle Paperwhite é um presente perfeito.
                Com tela antirreflexo e iluminação embutida, permite a leitura confortável em qualquer ambiente, mesmo sob a luz do sol.
                A bateria de longa duração e a capacidade de armazenar milhares de livros tornam-no ideal para viagens e momentos de relaxamento.

                Termo de busca 3: 'Fone de ouvido sem fio'
                Descrição: Um presente prático e versátil para pessoas de todas as idades.
                Fones de ouvido sem fio oferecem liberdade de movimento e qualidade de som, sendo perfeitos para ouvir música,
                podcasts ou atender chamadas enquanto realiza outras atividades. Escolha um modelo com bom isolamento de ruído e bateria de longa duração para uma experiência ainda melhor.

                Dica financeira 1: Não se deixe levar pela impulsividade! Antes de sair comprando o primeiro item que chamar sua atenção, pesquise e compare preços em diferentes lojas físicas e online.
                Utilize ferramentas de comparação de preços e fique atento a promoções e descontos. Lembre-se, o objetivo é encontrar o melhor presente pelo melhor preço, sem comprometer seu orçamento.

                Dica financeira 2: Se você já comprou um presente, mas está com dúvidas se a pessoa realmente vai gostar, não hesite em trocá-lo.
                Muitas lojas oferecem políticas de troca flexíveis, permitindo que você encontre algo mais adequado sem perder seu investimento.
                O importante é garantir que o presente seja significativo e traga alegria para quem o receber.
                """

                # --- Configurações do Gemini ---
                configurações = {
                    "candidate_count": 1,
                    "temperature": 0.75,
                    "top_k": 20,
                    "top_p": 0.95,
                }

                filtros = {
                    'HATE': 'BLOCK_NONE',
                    'HARASSMENT': 'BLOCK_NONE',
                    'SEXUAL': 'BLOCK_NONE',
                    'DANGEROUS': 'BLOCK_NONE'
                }

                model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                              generation_config=configurações,
                                              safety_settings=filtros,)

                response = model.generate_content(prompt)

                st.write("# 🤖 Sugestões do Gemini")
                st.markdown(response.text)

                # --- Extração de Termos de Busca ---
                termos_de_busca = []
                for linha in response.text.splitlines():
                    if linha.startswith("## "):
                        termos_de_busca.append(linha[3:])

                # --- Resultados do Mercado Livre ---
                st.header("🔍 Resultados do Mercado Livre")
                for termo in termos_de_busca:
                    st.subheader(termo)
                    resultados = pesquisar_mercado_livre(termo)
                    for produto in resultados:
                        st.write(f"[{produto['titulo']}]({produto['link']})")

else:
    st.warning("Por favor, insira sua API Key para continuar.")
