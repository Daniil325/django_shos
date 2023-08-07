import React, {useEffect, useState} from 'react';
import axios from "axios";
import {useParams} from "react-router-dom";

const Navbar = () => {

    const API_STATIC_MEDIA = "http://localhost:8000"
    const [appState, setAppState] = useState([]);

    let params = useParams();

    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/news/' + params.id)
            .then(data => {
                setAppState(data.data);
            })
    }, []);




    return (
        <div className="post-wrapper">
                {appState.map(el => {
                    return (
                        <div className="">

                            <h1 className="" href="">{el.header}</h1>


                            <p><img className="" src={API_STATIC_MEDIA + el.post_image} /></p>
                             <p>{el.message }</p>
                            <p className="">{el.pub_date}</p>
                        </div>
                    );
                })}
            </div>
    );


}

export default Navbar;