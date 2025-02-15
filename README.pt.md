# Verificador de Força de Senha

[🇬🇧 Read in English](README.md)

## Visão Geral

Este projeto implementa um **Verificador de Força de Senha** que avalia a segurança de uma senha fornecida, calculando sua **entropia** e estimando o tempo necessário para um hacker quebrá-la. O verificador também verifica se a senha foi exposta em vazamentos de dados conhecidos, consultando a **API Pwned Passwords**.

### Principais Funcionalidades:
- **Cálculo de Entropia**: Mede a força de uma senha com base em seu comprimento e na variedade de caracteres utilizados.
- **Estimativa de Tempo de Quebra**: Fornece uma estimativa de quanto tempo um hacker levaria para quebrar a senha usando técnicas comuns de cracking.
- **Verificação de Senhas Vazadas**: Confere se a senha foi comprometida em vazamentos de dados anteriores utilizando a **API Pwned Passwords**.

---

## Instalação

Para executar este projeto, é necessário ter o Python 3.x instalado. Além disso, você precisará do módulo `requests` para interagir com a API.

1. **Clone o repositório**:

```bash
git clone https://github.com/JeanVerissimo/password-strength-checker.git
cd password-strength-checker
```

2. **Instale as dependências**:

```bash
pip install requests
```

---

## Uso

Execute o script `main.py` para iniciar a verificação da força da senha. O script solicitará que você insira uma senha, calculará sua entropia, estimará o tempo de quebra e verificará se ela foi exposta em um vazamento de dados.

```bash
python main.py
```

Você será solicitado a digitar uma senha. A saída será semelhante ao seguinte exemplo:

```
#**************************************************
Checking entropy value... 
Entropy value: 56 bits.
Estimated time to crack password: less than 1 second.

Checking if this password has been found in data breaches...
This password was NOT found in data breaches
#**************************************************
```

Se a senha for encontrada no banco de dados da Pwned Passwords, você receberá uma notificação.

---

## Aviso Legal

Este projeto é apenas para fins educacionais. O verificador de força de senha não é uma ferramenta de segurança abrangente e não deve ser usado como único método de proteção para sistemas sensíveis. Sempre siga as melhores práticas de gerenciamento de senhas e utilize medidas de segurança adicionais, como a autenticação multifator (MFA).

