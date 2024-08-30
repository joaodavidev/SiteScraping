from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "Sua tarefa é extrair informações específicas do seguinte conteúdo de texto: {dom_content}. "
    "Por favor siga essas instruções atentamente: \n\n"
    "1. **Extrair informação:** Apenas extraia as informações que se ligam diretamente com a seguinte descrição: {parse_description}. "
    "2. **Sem informações extras:** Não inclua nenhuma informação adicional como texto, comentários ou explicações na sua resposta. "
    "3. **Resposta vazia:** Se nenhuma informação se liga com a descrição, retorne uma string vazia ('')."
    "4. **Apenas informações diretas:** Sua resposta deve conter somente informações que foram especificamente requisitadas, sem mais nenhum texto."
)

model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    prompt =  ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})

        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)
    
    return "\n".join(parsed_results)