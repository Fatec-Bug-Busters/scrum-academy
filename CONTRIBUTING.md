# Como Contribuir - Seu Passaporte de Entrada

Estamos felizes em receber você aqui e saber que está interessado em contribuir para o nosso projeto. Como um projeto de código aberto, cada contribuição é valorizada e ajuda a impulsionar o crescimento e a qualidade do nosso trabalho. Este guia foi criado para orientá-lo sobre como você pode participar e fazer parte da nossa comunidade de desenvolvimento. Estamos ansiosos para ver suas contribuições e trabalhar juntos para tornar nosso projeto ainda melhor!

## Código de Conduta

Para garantir um ambiente respeitável e inclusivo, leia e siga nosso [Código de Conduta](./CODE_OF_CONDUCT.md).

## Começando a Contribuir

Contribuir para o nosso projeto é fácil e estamos ansiosos para receber suas contribuições! Antes de entrarmos ns passos para instalação da aplicação, precisamos passar pela lista de requisitos. Você precisará dos seguintes programas e acessos para contribuir com a nossa aplicação:

- Uma conta no [GitHub](https://github.com/)
- O *version control system* [Git](https://git-scm.com/) instalado
- Um IDE para o desenvolvimento. Recomendamos o [Visual Studio Code](https://code.visualstudio.com/). Confira também as [extensões indicadas](#algumas-indicações-opcionais) para o VSCode.
- O interpretador da linguagem [Python](https://www.python.org/)
- E um navegador de sua escolha

Agora sim, aqui está um guia passo a passo sobre como você pode enviar suas contribuições de maneira eficaz:

1. Clone o Repositório

    ```sh
    git clone https://github.com/Fatec-Bug-Busters/scrum-academy.git
    ```

2. Navegue até o projeto

    ```sh
    cd scrum-academy
    ```

3. Indicamos o uso de um ambiente virtual, como o [venv](https://docs.python.org/3/library/venv.html)

    ```sh
    python -m venv venv

    # Windows
    source venv/Scripts/activate

    # Linux
    . venv/bin/activate

    # Mac
    source venv/bin/activate
    ```

4. Instale as dependências

    ```sh
    pip install -r requirements.txt
    ```

4. Configure o Banco de Dados MySQL

   Crie o banco de dados com o código em `scripts.sql`

   ```sh
   mysql -u root -p < scripts.sql
   # ou
   sudo mysql < scripts.sql
   ```

   Copie o arquivo `.env`

   ```sh
   # copie o arquivo .env
   cp .env.template .env
   ```

   Insira as informações do banco de dados no arquivo `.env`

   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASS=
   MYSQL_DB=scrumacademy
   ```

5. Rode o servidor Flask

    ```sh
    # rodar o projeto localmente
    flask run
    ```

6. Abra em um navegador: [http://localhost:5000](http://localhost:5000)

Com esses passos, você deve ter tudo pronto para começar a desenvolver.

## Enviando suas modificações

Quando tudo estiver pronto, **Abra um Pull Request** e descreva suas alterações. Tente seguir um padrão de estilo para facilitar o entendimento de outros colaboradores. As [extensões indicadas](#algumas-indicações-opcionais) para o VSCode podem ajudar com isso.

E é isso! Assim que recebermos o seu pull request, faremos o possível para revisá-lo e mesclá-lo o mais rápido possível. Obrigado por contribuir para o nosso projeto!

## Relatando Problemas e Solicitando Recursos

Se encontrar um bug ou tiver uma ideia para um novo recurso, adoraríamos saber! **Crie uma [Issue aqui](https://github.com/Fatec-Bug-Busters/scrum-academy/issues) no GitHub e Descreva o Problema ou a Solicitação**: seja claro e detalhado sobre o problema ou recurso desejado.

Fique Atualizado: Acompanhe sua issue para ver as discussões e atualizações sobre o problema ou recurso.

## Algumas indicações (Opcionais)

Para uma experiência de desenvolvimento mais suave, recomendamos o uso do Visual Studio Code e instalar as seguintes extensões do VSCode que vão facilitar nossa vida. São elas:

- [Auto Complete Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-complete-tag) - auto close HTML tags
- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) - Launch a development local Server with live reload feature
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - escreva markdown facilmente {markdown-all-in-one}
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) - Markdown linting and style checking
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - formata código CSS, JS etc.
- [IntelliSense for CSS class names](https://marketplace.visualstudio.com/items?itemName=Zignd.html-css-class-completion) - autocompleta classes (como do Bootstrap) - autocomplete classes found in your workspace or external files referenced through the link element.
- [CSS Auto prefix](https://marketplace.visualstudio.com/items?itemName=sporiley.css-auto-prefix) - Add propriedades CSS para compatibilidade com outros dispositivos
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) - correct spelling errors
- [Editorconfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) - styling
- [Git graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) - git graph
- [GitHub Pull Request](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Facilita a programação com Python - Microsoft's extension
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) - Destaca erros de digitação - Microsoft's extension
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) - formata o código (code styling)
- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) - sort the Python imports
- [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) - Doc string generator
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) - correct indentation
- [Jinja - Flask](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja) - Colore sintaxe do Jinja

Para instalar, abra o terminal no vscode e cole os seguintes comandos:

```sh
code --install-extension formulahendry.auto-complete-tag
code --install-extension ritwickdey.LiveServer
code --install-extension yzhang.markdown-all-in-one
code --install-extension DavidAnson.vscode-markdownlint
code --install-extension esbenp.prettier-vscode
code --install-extension Zignd.html-css-class-completion
code --install-extension sporiley.css-auto-prefix
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension EditorConfig.EditorConfig
code --install-extension mhutchie.git-graph
code --install-extension GitHub.vscode-pull-request-github
code --install-extension ms-python.python
code --install-extension ms-python.pylint
code --install-extension ms-python.black-formatter
code --install-extension ms-python.isort
code --install-extension njpwerner.autodocstring
code --install-extension KevinRose.vsc-python-indent
code --install-extension wholroyd.jinja
```

### Configurar as extensões

Aperte `Ctrl + Shift + P` no vscode, digite "User Settings JSON" e aperte em `Preferences: Open User Settings (JSON)`

Digite no início do arquivo após o símbolo `{`:

```json
    "[html]": {
      "editor.defaultFormatter": "vscode.html-language-features",
      "editor.formatOnSave": true
    },
    "[css]": {
      "editor.defaultFormatter": "vscode.css-language-features",
      "editor.formatOnSave": true
    },
    "[json]": {
      "editor.defaultFormatter": "vscode.json-language-features",
      "editor.formatOnSave": true
    },
    "pylint.lintOnChange": true,
    "[python]": {
      "editor.defaultFormatter": "ms-python.black-formatter",
      "editor.formatOnSave": true
    },
    "[markdown]": {
      "editor.defaultFormatter": "yzhang.markdown-all-in-one"
    },
```

## Commit de Gratidão

Ninguém faz nada sozinho, e cada contribuição importa! 🌟 A colaboração de cada um é essencial para avançarmos de forma sólida e construtiva. Vamos manter o bom trabalho e reconhecer cada passo que nos leva adiante. Obrigado por ajudar a melhorar o nosso sistema!

![Bug Busters](./src/static/images/bug-busters-logo-black.png)
![Bug Busters](./src/static/images/bug-busters-logo-white.png)
