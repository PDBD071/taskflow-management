function Tasks() {
  return (
    <div className="dashboard">

      <header className="topbar">
        <h1>TaskFlow</h1>

        <nav>
          <a href="/dashboard">Dashboard</a>
          <a href="/tasks">Tarefas</a>
          <a href="/">Sair</a>
        </nav>
      </header>


      <h2>
        TESTE TASKS NOVO
      </h2>

      <p>
        Aqui você poderá cadastrar e acompanhar suas tarefas.
      </p>


      <div className="cards">

        <div className="card">
          <h3>Total</h3>
          <span>0</span>
        </div>

        <div className="card">
          <h3>Pendentes</h3>
          <span>0</span>
        </div>

        <div className="card">
          <h3>Concluídas</h3>
          <span>0</span>
        </div>

      </div>

    </div>
  );
}

export default Tasks;