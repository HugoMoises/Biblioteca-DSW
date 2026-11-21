from django.core.exceptions import ValidationError

def validar_tamanho_arquivo(file):
    limite = 1 * 1024 * 1024 

    if file.size > limite:
        raise ValidationError('O arquivo não pode ultrapassar 1 MB.')