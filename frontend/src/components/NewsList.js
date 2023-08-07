import React, {useEffect, useState} from 'react';
import axios from "axios";

const NewsList = () => {

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
        <div className='content'>
            <h1>Список новостей</h1>
            <div className="news-wrapper">
                {appState.map(el => {
                    return (
                        <div className="news-item">
                            <img className="news-image" src={API_STATIC_MEDIA + el.post_image}/>
                            <p className="news-text">
                                <a className="news-link" href={"post/" + el.id}>{el.header}</a>
                            </p>
                            <p className="news-date">{el.pub_date}</p>
                        </div>
                    );
                })}
            </div>
        </div>
);


}

export default NewsList;