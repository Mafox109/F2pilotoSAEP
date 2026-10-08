Descrição do Funcionamento
O código implementa o estado legado do sistema de almoxarifado
Arquitetura Monolítica e Interface Terminal: O sistema roda em um único arquivo via menu interativo no terminal. Os dados dos materiais são armazenados em uma estrutura de lista de dicionários em memória durante a execução.
O Sistema agora conta com:
- Tela splash 
- Tela de Login
Operações de Login:
- Validação de usuario
- Funções separadas por nivel de herarquia de poder de login
- Nome de Usuario repassado a outras tela para melhor UX
Operações de CRUD MENU:
- Cadastrar: Permite inserir novos insumos definindo nome e quantidade inicial, gerando um ID incremental automático.
- Listar: Exibe no terminal todos os materiais cadastrados com seus respectivos IDs e saldos.
- Atualizar: Permite alterar o nome ou a quantidade de um material selecionado pelo ID.
- Excluir: Remove o registro do material do sistema a partir do seu ID.
Ausência de registro de data/hora ou de responsável pela operação.
