## Relacionamento Autor -> Livro

Foi utilizado "PROTECT" no on_delete no relacionamento entre Livro e Autor para impedir que um autor seja excluído se tiver um livro relacionado a ele. Isso evita que tenham livros cadastrados com o campo de autor nulo.