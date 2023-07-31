import React, {useEffect, useState} from 'react';
import axios from "axios";

const About = () => {

    const [appState, setAppState] = useState();

    useEffect(() => {
        const apiUrl = 'http://localhost:8000/api/country_info';
        axios.get(apiUrl).then((resp) => {
            const allPersons = resp.data;
            setAppState(allPersons);
        });
    }, [setAppState]);

    return (
        <div className="content">
            о сайте
        </div>
    )
}

export default About;