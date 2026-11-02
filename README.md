<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:fbcfe8,100:f9a8d4&height=170&section=header&text=Agente%20de%20Portf%C3%B3lio&fontSize=42&fontColor=831843&fontAlignY=42&desc=Google%20ADK%20%C2%B7%20Gemini%20%C2%B7%20MCP%20do%20GitHub&descSize=16&descAlignY=68" width="100%" />

<img src="https://readme-typing-svg.demolab.com?font=Quicksand&weight=600&size=19&pause=1400&color=DB2777&center=true&vCenter=true&width=620&lines=%22Liste+meus+reposit%C3%B3rios%22;%22Quais+projetos+est%C3%A3o+sem+README%3F%22;%22Analise+meu+c%C3%B3digo%22" />

</div>

<br>

### Sobre o projeto

Agente de IA que conversa com você e gerencia o seu perfil do GitHub: lista repositórios, analisa código e sugere como organizar e apresentar os projetos.

O agente não tem ferramentas escritas no código. Ele as recebe do **MCP (Model Context Protocol) oficial do GitHub**, que oferece ações como listar repositórios, ler arquivos e abrir issues. Assim, ganha novas capacidades sem mudar o código.

<br>

### Origem do projeto

Este projeto marca o meu **primeiro contato com inteligência artificial e agentes**.

Construí o agente no **Build with AI**, evento do **Google Developer Groups (GDG) de São Paulo**, em maio de 2026. O desenvolvimento foi um workshop prático: todos os participantes construíram o agente juntos, na mesma sala, com o acompanhamento da instrutora **Simara Conceição**.

Foi ali que aprendi o que é um agente, como ele escolhe e usa ferramentas e como conectar um modelo de linguagem a um serviço real, como o GitHub. Depois do evento, revisei o código, corrigi a execução pelo terminal e documentei o projeto.

<br>

### Como funciona

```
Você (terminal ou navegador)
        │
        ▼
Agente ADK · Gemini 2.5 Flash      decide qual ferramenta usar
        │
        ▼
Servidor MCP do GitHub  ──►  API do GitHub
```

<br>

### Tecnologias

<div align="center">
  <img src="https://skillicons.dev/icons?i=py,github&theme=light" />
  <br>
  <sub>Python · Google ADK · Gemini 2.5 Flash · MCP do GitHub</sub>
</div>

<br>

### Como executar

**1. Instalar**

```bash
git clone https://github.com/sosofisouza/agente-portfolio-github.git
cd agente-portfolio-github
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux e macOS
pip install -r requirements.txt
```

**2. Configurar as chaves**

Copie o `.env.example` para `my_agent/.env` e preencha:

- `GOOGLE_API_KEY`: gere no [Google AI Studio](https://aistudio.google.com/apikey)
- `GITHUB_TOKEN`: crie um *fine-grained token* no GitHub, só com as permissões necessárias

**3. Executar**

| Comando | O que abre |
|:---|:---|
| `adk web` | Interface no navegador, em `http://localhost:8000` |
| `adk run my_agent` | Conversa no terminal |
| `python main.py` | Conversa no terminal, pelo script do projeto |

<br>

### Estrutura

```
agente-portfolio-github/
├── my_agent/
│   ├── __init__.py
│   └── agent.py        definição do agente e conexão com o MCP do GitHub
├── main.py             execução pelo terminal com o Runner do ADK
├── requirements.txt
└── .env.example        modelo das variáveis de ambiente
```

<br>

### Segurança

- O `.env` está no `.gitignore` e nunca vai para o repositório.
- Use um token do GitHub com o mínimo de permissões. Para apenas consultar, leitura basta.

<br>

### Próximos passos

- Gerar automaticamente o README de repositórios que não têm
- Criar um relatório do portfólio com linguagens, projetos sem descrição e últimos commits

<br>

<img src="https://capsule-render.vercel.app/api?type=rounded&color=0:fbcfe8,100:f9a8d4&height=60&section=footer" width="100%" />
