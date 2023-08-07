import React from 'react';

const Navbar = () => {
    return (
        <div className="navbar">
            <p className="navbar-item"><a className="navbar-link" href="/">О сайте</a></p>
            <p className="navbar-item"><a className="navbar-link" href="/Map">Карта</a></p>
            <p className="navbar-item"><a className="navbar-link" href="/Dictionary">Интерактивный словарь</a></p>
            <p className="navbar-item"><a className="navbar-link" href="/newslist">Новости</a></p>
        </div>
    )
}

export default Navbar;