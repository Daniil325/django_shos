import React, {useEffect, useState} from 'react';
import axios from "axios";

const Navbar = () => {

    const API_STATIC_MEDIA = "http://localhost:8000"
    const [appState, setAppState] = useState([]);

    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/news')
            .then(data => {
                setAppState(data.data);
            })
    }, []);


    return (
        appState.map(el => {
                return (
                    <div>
                        <img src={API_STATIC_MEDIA + el.post_image}/>
                    </div>
                );
            })
    );


}

export default Navbar;