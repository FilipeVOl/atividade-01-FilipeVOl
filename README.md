[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZutgNvaB)
# Exercícios de TDD - Prática de Desenvolvimento Guiado por Testes

Este repositório contém exercícios práticos de TDD (Test-Driven Development) que abordam diferentes cenários do mundo real. O primeiro exercício será desenvolvido em conjunto, servindo como exemplo, e os demais serão implementados pelos alunos.

## Métodos de Execução

### 1. Usando GitHub Codespaces (Recomendado)

O GitHub Codespaces oferece um ambiente de desenvolvimento pronto para uso, sem necessidade de configuração local.

#### Como Usar:
1. Clique no botão "Code" no repositório
2. Selecione "Open with Codespaces"
3. Aguarde a inicialização do ambiente
4. O ambiente já vem com:
   - Python instalado
   - pytest e pytest-cov configurados
   - Extensões úteis do VS Code
   - Terminal integrado

#### Vantagens:
- Sem necessidade de instalar nada localmente
- Ambiente consistente para todos
- Configuração automática
- Acesso de qualquer dispositivo

### 2. Execução Local (Alternativa)

Se preferir executar localmente, siga estas instruções:

#### Pré-requisitos:
- Python 3.8 ou superior
- Git instalado
- Terminal/Command Prompt

#### Configuração:
1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   cd tdd-python
   ```

2. Crie um ambiente virtual (recomendado):
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install pytest pytest-cov
   ```

4. Verifique a instalação:
   ```bash
   pytest --version
   pytest-cov --version
   ```

## Exercícios Disponíveis

### 1. Sistema de Pagamento de Funcionários (Desenvolvido em Conjunto)
Este exercício será desenvolvido em conjunto como exemplo prático de TDD. Vamos implementar um sistema de cálculo de pagamento de funcionários considerando:

**Aspectos a serem testados:**
- Cálculo correto do salário base
- Adição do custo do empregador
- Cálculo de comissão
- Validação de valores negativos
- Tratamento de horas extras
- Cálculo de benefícios

**Arquivos:**
- `funcionario/funcionario.py`
- `funcionario/test_funcionario.py`

### 2. Sistema de Controle de Estoque (Exercício para Alunos)
Implemente um sistema de controle de estoque com os seguintes requisitos:

**Aspectos a serem testados:**
- Controle de quantidade (mínimo e máximo)
- Cálculo de valor total do estoque
- Controle de validade dos produtos
- Registro de movimentações
- Alertas de estoque baixo
- Cálculo de perdas

**Requisitos de Cobertura:**
- Mínimo de 100% de cobertura de código
- Testes para todos os métodos públicos
- Testes para casos de erro e exceções
- Testes para valores limite

**Arquivos:**
- `estoque/produto.py`
- `estoque/test_produto.py`

## Como Usar

### Para o Exercício de Funcionários (Desenvolvido em Conjunto)
1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install pytest pytest-cov
   ```
3. Navegue até a pasta `funcionario`
4. Execute os testes:
   ```bash
   pytest
   ```
5. Siga o desenvolvimento guiado pelo professor

### Para o Exercício de Estoque (Implementação Individual)
1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install pytest pytest-cov
   ```
3. Navegue até a pasta `estoque`
4. Implemente os testes e o código seguindo o ciclo TDD
5. Verifique a cobertura dos testes:
   ```bash
   pytest --cov=./ --cov-report=term-missing
   ```

## Critérios de Avaliação

O GitHub Actions irá analisar para cada exercício:
- Porcentagem de cobertura de código (mínimo 100%)
- Número de testes passados/falhados
- Porcentagem de testes passados
- Qualidade dos testes (completude e robustez)

## Metodologia TDD

Para cada exercício, siga o ciclo TDD:

1. **Red**: Escreva um teste que falha
2. **Green**: Faça o teste passar com o mínimo de código possível
3. **Refactor**: Melhore o código mantendo os testes passando

## Dicas para Implementação

1. Comece pelos casos mais simples
2. Mantenha os testes passando após cada mudança
3. Refatore o código quando necessário
4. Verifique a cobertura dos testes após cada implementação
5. Documente seu código com docstrings claras
6. Use type hints para melhor legibilidade
7. Pense em casos de borda e exceções
8. Mantenha os testes independentes entre si

## Entrega e Avaliação

1. Faça um fork deste repositório
2. Implemente o exercício de estoque
3. Certifique-se de que todos os testes passam
4. Verifique se a cobertura está acima de 100%
5. Faça um pull request com sua implementação
6. O professor avaliará:
   - Qualidade dos testes
   - Cobertura de código
   - Organização do código
   - Documentação
   - Seguimento do ciclo TDD

## Avaliação de Cobertura com GitHub Actions

O GitHub Actions está configurado para avaliar automaticamente a cobertura de testes de cada exercício. Aqui está como funciona:

### Processo de Avaliação

1. **Execução Automática**
   - Os testes são executados automaticamente a cada push
   - A cobertura é calculada para cada arquivo Python
   - Um relatório detalhado é gerado

2. **Métricas Analisadas**
   - **Cobertura Total**: Porcentagem de linhas de código cobertas por testes
   - **Cobertura por Arquivo**: Detalhamento da cobertura em cada arquivo
   - **Linhas Não Cobertas**: Identificação específica das linhas sem testes

3. **Visualização dos Resultados**
   - Os resultados são exibidos na aba "Actions" do GitHub
   - Um badge de cobertura é atualizado no README
   - Relatório detalhado disponível no artefato "test-report"

### Critérios de Aprovação

Para ser aprovado, seu código deve:
- Ter no mínimo 100% de cobertura total
- Ter todos os métodos públicos testados
- Ter testes para casos de erro e exceções
- Ter testes para valores limite

### Como Verificar Localmente

Antes de fazer push, você pode verificar a cobertura localmente:
```bash
# Ver cobertura geral
pytest --cov=./ --cov-report=term-missing

# Ver cobertura detalhada por arquivo
pytest --cov=./ --cov-report=html
```

### O que Fazer se a Cobertura Estiver Baixa

1. Verifique o relatório para identificar as linhas não cobertas
2. Adicione testes para os casos não cobertos
3. Execute os testes localmente para confirmar a melhoria
4. Faça push das alterações para atualizar a cobertura

### Exemplo de Badge de Cobertura

![Cobertura de Testes](https://img.shields.io/badge/coverage-100%25-green)

## Problemas Técnicos? Google it!

Se você está no 7º período e ainda não sabe usar o Google para resolver problemas básicos de Git/configuração, está na hora de aprender.

### Exemplo de Problema:
"AH NÃO SEI FAZER ISSO NO MEU COMPUTADOR"

### Solução:
1. [GOOGLE.COM](https://www.google.com)
2. Digite sua dúvida
3. Aplique a solução

### Exemplos de Buscas Úteis:
- "git config port 443"
- "git connection error"
- "git proxy settings"

### Dica Profissional:
Aprender a pesquisar é tão importante quanto aprender a programar. Stack Overflow, ChatGPT, documentação oficial são seus melhores amigos.

---

## Configurando Git via SSH na porta 443

A rede da Unievangelica bloqueia a porta padrão do SSH (22), você pode forçar o Git a usar a porta 443 editando o arquivo de configuração do SSH.

### Passos:

1. Acesse (ou crie) o arquivo `~/.ssh/config`
2. Adicione o seguinte conteúdo:

```bash
Host github.com
  HostName ssh.github.com
  Port 443
  User git
  IdentityFile ~/.ssh/id_rsa
```
