import React from 'react'
import { FiMenu, FiGithub } from 'react-icons/fi'
import landGif from '../../images/galtontab.gif'
import './style.css'


function Landing() {
    return (
        <div id="page-landing">
            <header className="page-header">
                <a className="menu" href="">
                    <FiMenu size="25px" />     
                </a>
                <a className="desenvolvedor" href="">
                    Desenvolvedor
                </a>
                <a href="">
                    Cadeia de Markov ?
                </a>
            </header>
            <main>
                <h1>MARKOV CHAINS</h1>
                <span>Gere textos a partir de tweets do Twitter utilizando Cadeias de Markov.</span>
                <span>Divirta-se!</span>
                <img src={landGif} width="310px" height="612px" alt="máquina de Galton"/>
            </main>
            <footer>
                <FiGithub/>
                <a href="https://github.com/KaioViana/analise-de-markov" target="blanck">
                    https://github.com/KaioViana/analise-de-markov
                </a>
                
            </footer>
        </div>
    )
} 

export default Landing