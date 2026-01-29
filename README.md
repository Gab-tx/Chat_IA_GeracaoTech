# 🕵️ Sherlock - Assistente Pessoal

Este projeto implementa um assistente virtual inteligente chamado **Sherlock**, utilizando a API oficial do Google Gemini. O Sherlock é focado em precisão, lógica e análise de dados, sendo guiado por uma instrução de sistema configurável via JSON.

---

## 🚀 Funcionalidades

* **Memória de Contexto:** Utiliza sessões de chat (`chats.create`) para lembrar de interações anteriores.
* **Instruções Dinâmicas:** Personalidade e regras de conduta carregadas a partir de um arquivo `config.json`.
* **Controle de Criatividade:** Configuração ajustada de `temperature` e `top_p` para respostas mais técnicas e menos aleatórias.
* **Interface Minimalista:** Loop de interação contínua via terminal.

---

## 🛠️ Pré-requisitos

Antes de começar, você precisará ter instalado:
* Python 3.10 ou superior
* Uma API Key do [Google AI Studio](https://aistudio.google.com/)

---

## 📦 Instalação

1. Clone o repositório ou baixe os arquivos.
2. Instale as dependências necessárias:
   ```bash
   pip install -U google-genai python-dotenv
