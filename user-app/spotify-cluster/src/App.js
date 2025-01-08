import './App.css';
import Home from './Home';
import Start from './Start';
import Layout from './Layout';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Clustering from './Clustering';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="start" element={<Start />} />
          <Route path="clustering/:id/:clusters" element={<Clustering />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
