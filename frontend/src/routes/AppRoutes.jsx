import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Tarefas from "../pages/Tarefas";


function AppRoutes() {
  return (
    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/dashboard" element={<Dashboard />} />

        <Route path="/tasks" element={<Tarefas />} />

      </Routes>

    </BrowserRouter>
  );
}

export default AppRoutes;