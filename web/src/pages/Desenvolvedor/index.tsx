import React from 'react'
import { Link } from 'react-router-dom'
import { FiTwitter, FiInstagram, FiLinkedin } from 'react-icons/fi'
import desenvolvedorImg from '../../images/desenvolvedor.svg'
import './style.css'


function Desenvolvedor() {
    return (
        <>
            <div id="desenvolvedor">
                <header>
                    <Link className="voltar-button" to="/">
                        voltar
                    </Link>
                </header>
                <main>
                    <img src={desenvolvedorImg} alt="desenvolvedor" />
                    <span>
                        Kaio César Viana de Oliveira Costa. Desenvolvedor RPA/Web, estudante de ciências da computação, data science, machinne learning e apaixonado por algoritmos.
                        Entusiasmado na área da programação  com conhecimentos nas liguagens e tecnologias Java, C#, JavaScript, Python e ReactJS.
                    </span>
                    <strong>
                        "A arte imita a vida e a programação imita a arte"
                    </strong>
                </main>
                <footer>
                    <span>Redes sociais</span>
                    <span className="decoration"></span>
                    <div>
                        <a href="https://twitter.com/KaioVia25836155/" target="blanck">
                            <FiTwitter size="40px"/>
                        </a>
                        <a href="https://www.instagram.com/kaiocesarviana/" target="blanck">
                            <FiInstagram size="40px"/>
                        </a>
                        <a href="https://www.linkedin.com/in/kaio-c%C3%A9sar-viana-de-oliveira-costa-46aa66162/" target="blanck">
                            <FiLinkedin size="40px"/>
                        </a>
                    </div>
                </footer>
            </div>
        </>
    )
}

export default Desenvolvedor