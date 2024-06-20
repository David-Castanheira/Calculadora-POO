# Calculadora-POO

## Visão Geral
Este projeto consiste em uma calculadora simples que executa operações matemáticas básicas como adição, subtração, multiplicação e divisão. O foco do projeto é aplicar os conceitos de orientação a objetos em Python utilizando o padrão de projeto Strategy, juntamente com a implementação de uma interface de usuário interativa com o framework React.js.

## Padrão de Projeto Strategy
O padrão de projeto Strategy permite definir uma família de algoritmos, encapsular cada um deles e torná-los intercambiáveis. Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam. No contexto da nossa calculadora, definimos estratégias para cada operação matemática, o que facilita a expansão e manutenção do código, pois novas operações podem ser adicionadas sem alterar o código existente.

## Estrutura do Projeto
O projeto está dividido em duas partes principais:
1. [**Back-end em Python**](https://www.python.org/doc/): Aqui, foi-se aplicado o padrão Strategy para criar classes responsáveis por cada operação matemática. Cada classe possui um método que executa a operação e todas seguem uma interface comum.
2. [**Front-end com React.js**](https://pt-br.legacy.reactjs.org): O front-end é uma aplicação React que fornece uma interface gráfica para a calculadora. Os usuários podem inserir valores, selecionar a operação desejada e receber o resultado calculado pelo back-end.

Obs: No caso deste projeto em um primeiro momento a interface não foi colocada como prioridade para que o foco fosse no funcionamento da calculadora

## Como Executar
Para executar o projeto, siga os passos abaixo:
1. Clone o repositório para sua máquina local.
2. Navegue até a pasta do back-end e instale as dependências necessárias.
3. Inicie o servidor back-end com `python app.py`.
4. Em uma nova janela do terminal, navegue até a pasta do front-end e instale as dependências com `npm install`.
5. Execute a aplicação React com `npm start`.
6. Abra o navegador e acesse `http://localhost:3000` para interagir com a calculadora.

## Contribuições
Contribuições são sempre bem-vindas! Se você tem uma ideia para melhorar a aplicação ou adicionar novas funcionalidades, sinta-se à vontade para criar um fork do projeto e enviar um pull request.
