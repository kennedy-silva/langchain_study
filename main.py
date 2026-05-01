from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableLambda
from pydantic import Field, BaseModel
from langchain.globals import set_debug
from dotenv import load_dotenv

set_debug(True)
load_dotenv()


# =========================
# MODELOS
# =========================

class Destino(BaseModel):
    cidade: str = Field(description="A cidade recomendada para visitar")
    motivo: str = Field(description="Motivo pelo qual visitar essa cidade")


class Restaurantes(BaseModel):
    cidade: str = Field(description="Cidade recomendada")
    restaurantes: str = Field(description="Restaurantes populares na cidade")


# =========================
# PARSERS
# =========================

parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)


# =========================
# PROMPTS
# =========================

prompt_cidade = PromptTemplate(
    template="""
Sugira uma cidade dado o meu interesse por {interesse}.

{formato_de_saida}
""",
    input_variables=["interesse"],
    partial_variables={
        "formato_de_saida": parseador_destino.get_format_instructions()
    }
)

prompt_restaurante = PromptTemplate(
    template="""
Sugira restaurantes populares entre locais em {cidade}.

{formato_de_saida}
""",
    input_variables=["cidade"],
    partial_variables={
        "formato_de_saida": parseador_restaurantes.get_format_instructions()
    }
)

prompt_cultural = PromptTemplate(
    template="Sugira atividades e locais culturais em {cidade}",
    input_variables=["cidade"]
)


# =========================
# MODELO
# =========================

modelo = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
)


# =========================
# CADEIAS
# =========================

cadeia_1 = prompt_cidade | modelo | parseador_destino
extrair_cidade = RunnableLambda(lambda x: {"cidade": x["cidade"]})
cadeia_2 = prompt_restaurante | modelo | parseador_restaurantes
cadeia_3 = prompt_cultural | modelo | StrOutputParser()


# encadeamento completo
cadeia = cadeia_1 | extrair_cidade | cadeia_2 | cadeia_3


# =========================
# EXECUÇÃO
# =========================

resposta = cadeia.invoke({
    "interesse": "praias"
})

print("\n📌 Resultado final:\n")
print(resposta)