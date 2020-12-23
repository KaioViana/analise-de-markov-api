import React, { CSSProperties } from 'react'
import markovChain from '../../images/markov_chain.gif'
import './style.css'


interface Style {
    style: CSSProperties
  }

function Load(props: Style) {
    return (
        <div id="load" style={props.style}>
            <main>
                <strong>GERANDO TEXTO...</strong>
                <img src={markovChain} width="425px" height="425px" alt="carregamento"/>
            </main>
        </div>
    )
}

export default Load
