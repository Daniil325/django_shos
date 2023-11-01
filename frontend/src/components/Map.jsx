import {VectorMap} from "@react-jvectormap/core";
import {worldMill} from "@react-jvectormap/world";
import React, {useEffect, useState} from "react";
import axios from "axios";
import About from "./About";
import AllNews from "./AllNews";


const WorldMap = () => {
    const [countries, setCountries] = useState([]);
    const [fff, setfff] = useState([]);


    let codes_list = []

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
        axios.get('http://127.0.0.1:8000/api/country_info').then(data => {
            setCountries(data.data);
        })
        axios.get('http://127.0.0.1:8000/api/news').then(eee => {
            setfff(eee.data);
        })
    }, []);

    return (
        <div className="wrapper">

            <div className="map_div">
                {countries.map(el => {

                    return (
                        <div className="info hide" id={el.code}>
                            Информация о стране
                            <p>Президент: {el.president}</p>
                            <p>Столица: {el.capital}</p>
                            <p>Язык: {el.language}</p>
                            <p>Валюта: {el.valuta}</p>
                            <h3>Новости</h3>
                            {fff.map(ell => {
                                if (ell.country === el.country){
                                    return(
                                        <ul>
                                            <li className="aaa_item"><a href={"post/" + ell.id}>{ell.header}</a></li>
                                        </ul>

                                    )
                                }
                            })}
                        </div>
                    );
                })}
                <VectorMap
                    map={worldMill}
                    backgroundColor="SkyBlue"

                    series={{
                        regions: [
                            {
                                values: {
                                    IN: "#f56d04",
                                    KZ: "#ec0327",
                                    TJ: "#03ecd9",
                                    RU: "#ffe9e9",
                                    KG: "#b93418",
                                    PK: "#016362",
                                    CN: "#b40f0f",
                                    UZ: "#049849",
                                }
                            }
                        ],
                    }}


                    onRegionTipShow={function regionalTip(event, label, code) {
                        return label.html(`
                  <div style="background-color: black; border-radius: 6px; min-height: 50px; width: 125px; color: white; padding-left: 10px">
                    <p>
                    <b>
                    ${label.html()}
                    </b>
                    </p>
                   
                    </div>`);
                    }}
                    onMarkerTipShow={function markerTip(event, label, code) {
                        return label.html(`
                  <div style="background-color: white; border-radius: 6px; min-height: 50px; width: 125px; color: black !important; padding-left: 10px>
                    <p style="color: black !important;">
                    <b>
                    ${label.html()}
                    </b>
                    </p>
                    </div>`);
                    }}

                    onRegionClick={function (event, code) {
                        const countries_codes = ["RU", "KZ", "CN", "IN", "TJ", "KG", "PK", "UZ"]
                        if (countries_codes.includes(code)) {

                            codes_list.push(code);

                            let country_info = document.getElementById(code);

                            country_info.classList.remove('hide');

                            if (codes_list.length === 2) {
                                let country_info = document.getElementById(codes_list[0]);
                                country_info.classList.add('hide');
                                codes_list.shift();
                            }
                        }

                    }}

                />
            </div>

        </div>

    );
}

export default WorldMap;