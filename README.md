## Relacionamento Autor -> Livro
No relacionamento ForeignKey entre Livro e Autor deve ser utilizado "PROTECT" no on_delete  para impedir que um autor seja excluído se tiver um livro relacionado a ele. Isso evita que tenham livros cadastrados com o campo de autor nulo.

### 1. Que dados se perdem quando a migração é revertida? Por quê?
Ao reverter a migração, os vínculos entre livros e autores podem ser perdidos. Isso acontece porque os relacionamentos foram copiados para o `ManyToManyField`, mas não existe uma função reversa para copiá-los de volta ao `ForeignKey` antigo.

### 2. Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?

O livro continua existindo, mas fica sem autor associado. Para evitar isso, podemos validar se há pelo menos um autor associado ao livro e lançar um ValidationError caso contrário. Essa validação deve ocorrer após salvar os relacionamentos, pois o ManyToManyField é armazenado separadamente do livro.