// Função de validação da senha no login
function validarSenha() {
    const senha = document.getElementById('senha').value;

    if (senha.length < 6) {
        alert('A senha deve ter pelo menos 6 caracteres!');
        return false;
    }
    if (!/\d/.test(senha)) {
        alert('A senha deve conter pelo menos um número!');
        return false;
    }
    if (!/[A-Z]/.test(senha)) {
        alert('A senha deve conter pelo menos uma letra maiúscula!');
        return false;
    }
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(senha)) {
        alert('A senha deve conter pelo menos um caractere especial!');
        return false;
    }
    return true; 
}
