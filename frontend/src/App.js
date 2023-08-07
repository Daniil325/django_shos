import './App.css';
import React from "react";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Map from "./components/Map";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Dictionary from "./components/Dictionary";
import About from "./components/About";
import NotFound from "./components/NotFound";
import NewsList from "./components/NewsList";

const App = () => {
    return (
        <BrowserRouter>
            <div className="main-wrapper">
                <Header/>
                <main className="main">
                    <Navbar/>
                    <Routes>
                        <Route path='/map' element={<Map/>}/>
                        <Route path='/dictionary' element={<Dictionary/>}/>
                        <Route path='/' element={<About/>}/>
                        <Route path='*' element={<NotFound/>}/>
                        <Route path='/post' element={<NewsList/>}/>
                    </Routes>
                </main>
            </div>
        </BrowserRouter>
    )
}

export default App;
