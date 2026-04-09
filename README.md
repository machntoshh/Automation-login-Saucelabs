### ID - TEST_SWAGLABS
### Title - # 🧪 Automação de Testes — SauceDemo Login

> **Site alvo:** [saucedemo.com](https://www.saucedemo.com/)  
> **Framework:** Selenium 4.x + Python  
> **Tipo:** E2E — Smoke Test de Autenticação  
> **Última atualização:** 09/04/2026

---

## 📋 Índice

- [Objetivo](#objetivo)
- [Pré-requisitos](#pré-requisitos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Casos de Teste](#casos-de-teste)
  - [TC-001 — Login e logout com standard\_user](#tc-001--login-e-logout-com-standard_user)
  - [TC-002 — Login e logout com problem\_user](#tc-002--login-e-logout-com-problem_user)
  - [TC-003 — Login e logout com performance\_glitch\_user](#tc-003--login-e-logout-com-performance_glitch_user)
  - [TC-004 — Login e logout com error\_user](#tc-004--login-e-logout-com-error_user)
  - [TC-005 — Login e logout com visual\_user](#tc-005--login-e-logout-com-visual_user)
  - [TC-006 — Login com locked\_out\_user (bloqueado)](#tc-006--login-com-locked_out_user-bloqueado)
  - [TC-007 — Login com senha inválida](#tc-007--login-com-senha-inválida)
  - [TC-008 — Login com campos vazios](#tc-008--login-com-campos-vazios)
- [Resumo da Execução](#resumo-da-execução)
- [Dados de Teste](#dados-de-teste)
- [Seletores Utilizados](#seletores-utilizados)
- [Melhorias Futuras](#melhorias-futuras)

---

## Objetivo

Validar o fluxo completo de **login → acesso ao inventário → logout** para todos os usuários disponíveis no SauceDemo. O script percorre cada usuário automaticamente, garantindo que o ciclo de autenticação funciona de ponta a ponta.

---

## Pré-requisitos

| Requisito         | Versão mínima | Instalação                          |
| ----------------- | ------------- | ----------------------------------- |
| **Python**        | 3.9+          | [python.org](https://python.org)    |
| **Google Chrome** | 120+          | Atualizar pelo navegador            |
| **ChromeDriver**  | Compatível    | Gerenciado automaticamente pelo Selenium 4.6+ |
| **Selenium**      | 4.x           | `pip install selenium`              |

### Instalação rápida

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/saucedemo-automation.git
cd saucedemo-automation

# Instalar dependências
pip install selenium
```

---

## Estrutura do Projeto

```
saucedemo-automation/
├── tests/
│   └── test_login_logout.py     # Script principal de automação
├── README.md                    # Este arquivo
└── requirements.txt             # Dependências (selenium)
```

---

## Como Executar

```bash
# Execução direta
python tests/test_login_logout.py

# Saída esperada no terminal
# (navegador abre, percorre cada usuário e fecha)
# Automação concluida...
```

---

## Casos de Teste

---

### TC-001 — Login e logout com standard\_user

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-001                                                             |
| **Tipo**             | Smoke / Funcional                                                  |
| **Prioridade**       | 🔴 Alta                                                           |
| **Pré-condições**    | Site acessível, navegador Chrome disponível                        |
| **Resultado Esperado** | Login realizado, página de inventário carregada, logout com sucesso |
| **Status**           | ✅ Passou                                                          |

**Passos:**

1. Acessar `https://www.saucedemo.com/`
2. Preencher campo username com `standard_user`
3. Preencher campo password com `secret_sauce`
4. Clicar no botão "Login"
5. Aguardar carregamento da lista de inventário (`inventory_list`)
6. Clicar no menu hambúrguer (☰)
7. Aguardar menu lateral ficar visível
8. Clicar em "Logout"
9. Validar retorno à tela de login

<details>
<summary>💻 Código executado</summary>

```python
username_login = driver.find_element(By.XPATH, '//*[@type="text"]')
password_login = driver.find_element(By.XPATH, '//*[@type="password"]')
botao_login = driver.find_element(By.XPATH, '//*[@type="submit"]')

username_login.send_keys("standard_user")
password_login.send_keys("secret_sauce")
botao_login.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
)

menu_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
)
menu_btn.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@class='bm-item-list']"))
)

logout_homepage = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
logout_homepage.click()
```

</details>

---

### TC-002 — Login e logout com problem\_user

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-002                                                             |
| **Tipo**             | Funcional / Exploratório                                           |
| **Prioridade**       | 🟡 Média                                                          |
| **Pré-condições**    | Site acessível, navegador Chrome disponível                        |
| **Resultado Esperado** | Login realizado. Inventário carregado (imagens podem estar quebradas). Logout com sucesso. |
| **Status**           | ⚠️ Passou com ressalva                                            |

**Passos:** Mesmos do TC-001, substituindo o username por `problem_user`.

**Observação:** Este usuário é propositalmente "problemático" no SauceDemo — as imagens dos produtos aparecem incorretas. O fluxo de login/logout funciona, mas a página apresenta bugs visuais intencionais.

---

### TC-003 — Login e logout com performance\_glitch\_user

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-003                                                             |
| **Tipo**             | Funcional / Performance                                            |
| **Prioridade**       | 🟡 Média                                                          |
| **Pré-condições**    | Site acessível, navegador Chrome disponível                        |
| **Resultado Esperado** | Login realizado com delay perceptível. Inventário carregado. Logout com sucesso. |
| **Status**           | ✅ Passou                                                          |

**Passos:** Mesmos do TC-001, substituindo o username por `performance_glitch_user`.

**Observação:** Este usuário simula lentidão no carregamento. O `WebDriverWait` com timeout de 10s cobre esse cenário, mas em conexões lentas pode ser necessário aumentar o timeout.

---

### TC-004 — Login e logout com error\_user

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-004                                                             |
| **Tipo**             | Funcional / Negativo                                               |
| **Prioridade**       | 🟡 Média                                                          |
| **Pré-condições**    | Site acessível, navegador Chrome disponível                        |
| **Resultado Esperado** | Login realizado. Inventário carregado (ações no carrinho podem falhar). Logout com sucesso. |
| **Status**           | ⚠️ Passou com ressalva                                            |

**Passos:** Mesmos do TC-001, substituindo o username por `error_user`.

**Observação:** Este usuário gera erros ao interagir com funcionalidades do carrinho e filtros. O fluxo de login/logout funciona normalmente.

---

### TC-005 — Login e logout com visual\_user

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-005                                                             |
| **Tipo**             | Funcional / Visual                                                 |
| **Prioridade**       | 🔵 Baixa                                                          |
| **Pré-condições**    | Site acessível, navegador Chrome disponível                        |
| **Resultado Esperado** | Login realizado. Inventário carregado (layout pode estar desalinhado). Logout com sucesso. |
| **Status**           | ⚠️ Passou com ressalva                                            |

**Passos:** Mesmos do TC-001, substituindo o username por `visual_user`.

**Observação:** Este usuário apresenta inconsistências visuais no layout (elementos desalinhados, ícones diferentes). Ideal para testes de regressão visual com ferramentas como Percy ou Applitools.

---

### TC-006 — Login com locked\_out\_user (bloqueado)

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-006                                                             |
| **Tipo**             | Funcional / Negativo                                               |
| **Prioridade**       | 🔴 Alta                                                           |
| **Pré-condições**    | Site acessível                                                     |
| **Resultado Esperado** | Login é bloqueado. Mensagem de erro: "Epic sadface: Sorry, this user has been locked out." |
| **Status**           | 🔲 Não implementado                                               |

**Passos:**

1. Acessar `https://www.saucedemo.com/`
2. Preencher campo username com `locked_out_user`
3. Preencher campo password com `secret_sauce`
4. Clicar no botão "Login"
5. Validar que a mensagem de erro é exibida
6. Validar que o usuário permanece na tela de login

<details>
<summary>💻 Sugestão de implementação</summary>

```python
def test_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH, '//*[@type="text"]').send_keys("locked_out_user")
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert "locked out" in error_msg.text.lower()
```

</details>

---

### TC-007 — Login com senha inválida

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-007                                                             |
| **Tipo**             | Funcional / Negativo                                               |
| **Prioridade**       | 🔴 Alta                                                           |
| **Pré-condições**    | Site acessível                                                     |
| **Resultado Esperado** | Mensagem de erro: "Epic sadface: Username and password do not match any user in this service" |
| **Status**           | 🔲 Não implementado                                               |

**Passos:**

1. Acessar a página de login
2. Preencher username com `standard_user`
3. Preencher password com `senha_errada`
4. Clicar em "Login"
5. Validar mensagem de erro

<details>
<summary>💻 Sugestão de implementação</summary>

```python
def test_senha_invalida(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH, '//*[@type="text"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("senha_errada")
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert "do not match" in error_msg.text.lower()
```

</details>

---

### TC-008 — Login com campos vazios

| Campo                | Detalhes                                                           |
| -------------------- | ------------------------------------------------------------------ |
| **ID**               | TC-008                                                             |
| **Tipo**             | Funcional / Validação                                              |
| **Prioridade**       | 🟡 Média                                                          |
| **Pré-condições**    | Site acessível                                                     |
| **Resultado Esperado** | Mensagem de erro: "Epic sadface: Username is required"            |
| **Status**           | 🔲 Não implementado                                               |

**Passos:**

1. Acessar a página de login
2. Não preencher nenhum campo
3. Clicar em "Login"
4. Validar mensagem de erro sobre campo obrigatório

<details>
<summary>💻 Sugestão de implementação</summary>

```python
def test_campos_vazios(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )
    assert "Username is required" in error_msg.text
```

</details>

---

## Resumo da Execução

| Status               | Qtd | Test Cases                          |
| -------------------- | --- | ----------------------------------- |
| ✅ Passou            | 2   | TC-001, TC-003                      |
| ⚠️ Passou c/ ressalva | 3   | TC-002, TC-004, TC-005              |
| 🔲 Não implementado  | 3   | TC-006, TC-007, TC-008              |
| **Total**            | **8** |                                   |

---

## Dados de Teste

Todos os usuários utilizam a mesma senha: `secret_sauce`

| Usuário                      | Comportamento esperado                              |
| ---------------------------- | --------------------------------------------------- |
| `standard_user`              | Fluxo normal, sem bugs                              |
| `locked_out_user`            | Bloqueado — não consegue logar                      |
| `problem_user`               | Imagens dos produtos incorretas                     |
| `performance_glitch_user`    | Lentidão proposital no carregamento                 |
| `error_user`                 | Erros ao interagir com carrinho e filtros            |
| `visual_user`                | Layout desalinhado e inconsistências visuais         |

---

## Seletores Utilizados

| Elemento             | Tipo     | Seletor                                          |
| -------------------- | -------- | ------------------------------------------------ |
| Campo username       | XPATH    | `//*[@type="text"]`                              |
| Campo password       | XPATH    | `//*[@type="password"]`                          |
| Botão Login          | XPATH    | `//*[@type="submit"]`                            |
| Lista de inventário  | CLASS    | `inventory_list`                                 |
| Menu hambúrguer (☰)  | ID       | `react-burger-menu-btn`                          |
| Menu lateral         | XPATH    | `//*[@class='bm-item-list']`                     |
| Link Logout          | XPATH    | `//a[@id="logout_sidebar_link"]`                 |
| Mensagem de erro     | CSS      | `[data-test="error"]`                            |

---

> **Nota:** Este projeto utiliza o [SauceDemo](https://www.saucedemo.com/) como ambiente de prática. É um site criado pela Sauce Labs especificamente para treinar automação de testes.

🤖 **README feito com a ajuda do Claude.ai usando o modelo Opus 4.6**
