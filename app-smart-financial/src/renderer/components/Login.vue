<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    onSubmit() {
      console.log('Usuário:', this.username, 'Senha:', this.password);
      this.$router.push('/main');
    },
    recoverPassword() {
      alert('Redirecionar para recuperação de senha');
    },
  },
};
</script>
<template>
  <div id="app" class="container">
    <div class="login-box">
      <h2>$mart Finance</h2>
      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="username">Usuário</label>
          <input
              v-model="username"
              id="username"
              type="text"
              placeholder="Digite seu usuário"
          />
        </div>
        <div class="form-group">
          <label for="password">Senha</label>
          <input
              v-model="password"
              id="password"
              type="password"
              placeholder="Digite sua senha"
          />
        </div>
        <button type="submit">Entrar</button>
      </form>
      <div class="recover">
        <a href="#" @click="recoverPassword">Esqueceu sua senha?</a>
      </div>
    </div>
  </div>
</template>
<style scoped>
/* Estilos básicos */
html,
body {
  margin: 0;
  height: 100%;
  font-family: Arial, sans-serif;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.login-box {
  background: var(--container-color);
  padding: 20px 30px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 300px;
  text-align: center;
}

h2 {
  margin-bottom: 20px;
  font-size: 24px;
  font-weight: bold;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
  font-size: 14px;
  color: #333;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

button {
  width: 100%;
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 10px;
}

button:hover {
  background: #0056b3;
}

.recover {
  margin-top: 10px;
}

.recover a {
  font-size: 14px;
  color: #007bff;
  text-decoration: none;
}

.recover a:hover {
  text-decoration: underline;
}
</style>
