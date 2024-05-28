import React from 'react'

export default function Navbar() {
    return (
        <div className = "Navbar">
            <a href="https://www.boeing.com"><img id="boeing-logo" src={require('./assets/BoeingLogo.png')} alt="boeing"/></a>
            <a href="/" id="navbar-title"><h1>NLP Assisted Maintenance Records</h1></a>
            <a href="https://www.nd.edu"><img id="nd-logo"src={require('./assets/NotreDame.png')} alt="nd" /></a>
        </div>
    )
}