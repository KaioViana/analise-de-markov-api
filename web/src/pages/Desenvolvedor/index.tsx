import React from 'react'
import { Link } from 'react-router-dom'
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
                    <img src={desenvolvedorImg} alt="desenvolvedor"/>
                    <span>
                        Kaio César Viana de Oliveira Costa. Desenvolvedor RPA/Web, estudante de ciências da computação, data science, machinne learning e apaixonado por algoritmos.
                        Entusiasmado na área da programação  com conhecimentos nas liguagens e tecnologias Java, C#, JavaScript, Python e ReactJS.
                    </span>
                    <strong>
                        "A arte imita a vida e a programação imita a arte"
                    </strong>
                </main>
            </div>
        </>
    )
}

export default Desenvolvedor