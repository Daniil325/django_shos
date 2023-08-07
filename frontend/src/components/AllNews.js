import React, {useEffect, useState} from 'react';
import axios from "axios";

const AllNews = () => {

    const [appState, setAppState] = useState([]);

    const countries_id = {
        1: "RU",
        2: "KZ",
        3: "CN",
        4: "IN",
        5: "TJ",
        6: "UZ",
        7: "PK",
        8: "KG"
    }

    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/news')
            .then(data => {
                setAppState(data.data);
            })
    }, []);


    return (
        <div className='content'>
            {appState.map(el => {
                return (
                    <ul className={countries_id[el.id]}>
                        <li>{el.header}</li>
                    </ul>
                );
            })}
        </div>
    );


}

export default AllNews;