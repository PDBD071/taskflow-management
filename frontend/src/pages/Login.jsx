import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function fazerLogin() {
    try {
      const resposta = await fetch(
        "http://127.0.0.1:8000/usuarios/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email,
            password,
          }),
        }
      );

      const dados = await resposta.json();

      if (!resposta.ok) {
        alert(dados.detail);
        return;
      }

      localStorage.setItem(
        "token",
        dados.access_token
      );

      navigate("/dashboard");

    } catch (erro) {
      alert("Erro ao conectar com o servidor.");
      console.error(erro);
    }
  }

  return (
    <div className="container">
      <h1>TaskFlow</h1>

      <p className="subtitle">
        Organize suas tarefas
      </p>

      <p className="welcome">
        Bem-vindo de volta!
      </p>

      <input
        type="email"
        placeholder="Digite seu e-mail"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Digite sua senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={fazerLogin}>
        Entrar
      </button>
    </div>
  );
}

export default Login;