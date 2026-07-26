import { useEffect, useState } from "react";


function Tarefas() {


  const [tarefas, setTarefas] = useState([]);

  const [titulo, setTitulo] = useState("");

  const [descricao, setDescricao] = useState("");

  const [dataConclusao, setDataConclusao] = useState("");

  const [tarefaEditando, setTarefaEditando] = useState(null);


  const [mensagem, setMensagem] = useState("");

  const [tipoMensagem, setTipoMensagem] = useState("");





  function mostrarMensagem(texto, tipo) {

    setMensagem(texto);

    setTipoMensagem(tipo);


    setTimeout(() => {

      setMensagem("");

      setTipoMensagem("");

    }, 3000);

  }






  async function carregarTarefas() {


    const token = localStorage.getItem("token");


    const resposta = await fetch(
      "http://127.0.0.1:8000/tarefas/",
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );


    const dados = await resposta.json();


    setTarefas(dados);


  }







  useEffect(() => {


    carregarTarefas();


  }, []);









  async function criarTarefa() {


    const token = localStorage.getItem("token");



    const resposta = await fetch(
      "http://127.0.0.1:8000/tarefas/",
      {
        method: "POST",

        headers: {

          "Content-Type": "application/json",

          Authorization: `Bearer ${token}`,

        },


        body: JSON.stringify({

          titulo,

          descricao,

          concluida: false,

          data_conclusao: dataConclusao || null,

        }),

      }
    );



    if (resposta.ok) {


      mostrarMensagem(
        "Tarefa criada com sucesso!",
        "sucesso"
      );


      setTitulo("");

      setDescricao("");

      setDataConclusao("");

      carregarTarefas();


    } else {


      mostrarMensagem(
        "Erro ao criar a tarefa.",
        "erro"
      );


    }


  }









  async function atualizarTarefa() {


    const token = localStorage.getItem("token");



    const tarefaAtual = tarefas.find(
      (tarefa) => tarefa.id === tarefaEditando
    );



    const resposta = await fetch(
      `http://127.0.0.1:8000/tarefas/${tarefaEditando}`,
      {

        method: "PUT",


        headers: {

          "Content-Type": "application/json",

          Authorization: `Bearer ${token}`,

        },


        body: JSON.stringify({

          titulo,

          descricao,

          concluida: tarefaAtual.concluida,

          data_conclusao: dataConclusao || null,

        }),


      }
    );



    if (resposta.ok) {


      mostrarMensagem(
        "Tarefa atualizada com sucesso!",
        "sucesso"
      );


      setTitulo("");

      setDescricao("");

      setDataConclusao("");

      setTarefaEditando(null);

      carregarTarefas();


    } else {


      mostrarMensagem(
        "Erro ao atualizar a tarefa.",
        "erro"
      );


    }


  }






  function editarTarefa(tarefa) {


    setTitulo(tarefa.titulo);

    setDescricao(tarefa.descricao);

    setDataConclusao(
      tarefa.data_conclusao || ""
    );

    setTarefaEditando(tarefa.id);


  }

  async function alterarConclusao(tarefa) {


    const token = localStorage.getItem("token");



    const resposta = await fetch(
      `http://127.0.0.1:8000/tarefas/${tarefa.id}`,
      {

        method: "PUT",


        headers: {

          "Content-Type": "application/json",

          Authorization: `Bearer ${token}`,

        },


        body: JSON.stringify({

          titulo: tarefa.titulo,

          descricao: tarefa.descricao,

          concluida: !tarefa.concluida,

          data_conclusao: tarefa.data_conclusao || null,

        }),


      }
    );



    if (resposta.ok) {


      mostrarMensagem(

        tarefa.concluida

          ? "Tarefa reaberta com sucesso!"

          : "Tarefa concluída com sucesso!",

        "sucesso"

      );


      carregarTarefas();


    } else {


      mostrarMensagem(
        "Erro ao alterar o status da tarefa.",
        "erro"
      );


    }


  }









  async function excluirTarefa(id) {


    const token = localStorage.getItem("token");



    const resposta = await fetch(
      `http://127.0.0.1:8000/tarefas/${id}`,
      {

        method: "DELETE",

        headers: {

          Authorization: `Bearer ${token}`,

        },

      }
    );



    if (resposta.ok) {


      mostrarMensagem(
        "Tarefa excluída com sucesso!",
        "sucesso"
      );


      carregarTarefas();


    } else {


      mostrarMensagem(
        "Erro ao excluir a tarefa.",
        "erro"
      );


    }


  }









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








      <h2 className="titulo-secao">
        Minhas Tarefas
      </h2>






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






      <div className="task-area">


        <h2>

          {
            tarefaEditando
              ? "Editar Tarefa"
              : "Nova Tarefa"
          }

        </h2>





        {
          mensagem && (

            <div
              className={
                tipoMensagem === "sucesso"
                  ? "mensagem sucesso"
                  : "mensagem erro"
              }
            >

              {mensagem}

            </div>

          )
        }





        <div className="task-form">

        <input

          type="text"

          placeholder="Título da tarefa"

          value={titulo}

          onChange={(e) => setTitulo(e.target.value)}

        />





        <input

          type="text"

          placeholder="Descrição da tarefa"

          value={descricao}

          onChange={(e) => setDescricao(e.target.value)}

        />





        <input

          type="date"

          value={dataConclusao}

          onChange={(e) => setDataConclusao(e.target.value)}

        />






        <button

          onClick={
            tarefaEditando
              ? atualizarTarefa
              : criarTarefa
          }

        >

          {
            tarefaEditando
              ? "Salvar Alteração"
              : "Criar Tarefa"
          }


        </button>


        </div>


      </div>









      <h2 className="titulo-secao">
        Lista de tarefas
      </h2>








      <div className="tasks-list">


        {

          tarefas.map((tarefa) => (


            <div

              className="task-card"

              key={tarefa.id}

            >




              <h3>
                {tarefa.titulo}
              </h3>





              <p>
                {tarefa.descricao}
              </p>





              <p>

                📅 Data:{" "}

                {
                  tarefa.data_conclusao

                    ? tarefa.data_conclusao

                    : "Sem data definida"
                }

              </p>







              <span>

                {
                  tarefa.concluida

                    ? "Concluída ✅"

                    : "Pendente ⏳"
                }

              </span>







              <div>


                <button

                  onClick={() => editarTarefa(tarefa)}

                >

                  Editar

                </button>







                <button

                  onClick={() => alterarConclusao(tarefa)}

                >

                  {
                    tarefa.concluida

                      ? "Reabrir"

                      : "Concluir"
                  }


                </button>







                <button

                  onClick={() => excluirTarefa(tarefa.id)}

                >

                  Excluir

                </button>



              </div>





            </div>


          ))

        }


      </div>






    </div>


  );


}



export default Tarefas;