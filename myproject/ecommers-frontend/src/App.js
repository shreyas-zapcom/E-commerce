import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
    const [searchQuery, setSearchQuery] = useState("");

    const handleSearch = (e) => {
        e.preventDefault();
        console.log("Searching for:", searchQuery);
        // Implement your search functionality here
    };

    return ( <
        div className = "App" >
        <header className = "App-header" >
        <
        img src = { logo }
        className = "App-logo"
        alt = "logo" / >
        <
        p >
        Edit < code > src / App.js < /code> and save to reload. < /
        p > <
        a className = "App-link"
        href = "https://reactjs.org"
        target = "_blank"
        rel = "noopener noreferrer" >
        Learn React <
        /a>

        { /* Welcome Message */ } <
        h1 > Welcome to Ecommerceee < /h1>

        { /* Search Bar */ } <
        form onSubmit = { handleSearch }
        className = "search-form" >
        <
        input type = "text"
        placeholder = "Search for products..."
        value = { searchQuery }
        onChange = {
            (e) => setSearchQuery(e.target.value)
        }
        className = "search-input" /
        >
        <
        button type = "submit"
        className = "search-button" >
        Search <
        /button> < /
        form > <
        /header> < /
        div >
    );
}

export default App;