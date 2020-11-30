import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { FiGithub, FiMenu } from 'react-icons/fi'
import Menu from '../../components/Menu/index'
import landGif from '../../images/galtontab.gif'
import './style.css'


function Landing() {
    const [slidingMenu, setSlidingMenu] = useState<boolean>(false)

    const slideMenu = () => {
        return slidingMenu ? { width: '39vw' } : { marginLeft: '-1000px' }
    }

    const menuButtonCliked = () => {
        setSlidingMenu(!slidingMenu)
    }

    return (
        <div id="page-landing">
            <header>
                <button onClick={() => { menuButtonCliked() }}>
                    <FiMenu size="25px" />     
                </button>
                <Link className="desenvolvedor" to="/desenvolvedor">
                    Desenvolvedor
                </Link>
                <Link to="">
                    Cadeia de Markov ?
                </Link>
            </header>
            <Menu style={slideMenu()}/>
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