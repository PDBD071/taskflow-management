import { useEffect, useState } from "react";

function Dashboard() {

  const [tarefas, setTarefas] = useState([]);


  useEffect(() => {

    async function carregarTarefas() {

      const token = localStorage.getItem("token");


      const resposta = await fetch(
        "http://127.0.0.1:8000/tarefas/",
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );


      const dados = await resposta.json();

      setTarefas(dados);

    }


    carregarTarefas();

  }, []);



  const total = tarefas.length;


  const pendentes = tarefas.filter(
    (tarefa) => !tarefa.concluida
  ).length;


  const concluidas = tarefas.filter(
    (tarefa) => tarefa.concluida
  ).length;



  return (
    <div className="dashboard">

      <header className="topbar">

        <h1>
          TaskFlow
        </h1>


        <nav>

          <a href="/dashboard">
            Dashboard
          </a>

          <a href="/tasks">
            Tarefas
          </a>

          <a href="/">
            Sair
          </a>

        </nav>

      </header>



      <h2>
        Olá, usuário!
      </h2>


      <p>
        Aqui está o resumo das suas tarefas.
      </p>



      <div className="cards">


        <div className="card">

          <h3>
            Total
          </h3>

          <span>
            {total}
          </span>

        </div>



        <div className="card">

          <h3>
            Pendentes
          </h3>

          <span>
            {pendentes}
          </span>

        </div>



        <div className="card">

          <h3>
            Concluídas
          </h3>

          <span>
            {concluidas}
          </span>

        </div>


      </div>


    </div>
  );
}


export default Dashboard;