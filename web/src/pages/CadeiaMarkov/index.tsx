import React from 'react'
import { Link } from 'react-router-dom'
import andreiMarkov from '../../images/andrei_markov.svg'
import './style.css'


function CadeiMarkov() {
    return (
        <>
            <div id="cadeia-markov">
                <header>
                    <Link to="/">
                        voltar
                    </Link>
                </header>
                <main>
                    <span>
                        Andrei Andreyevich Markov (14 de junho de 1856 — São Petersburgo, 20 de julho de 1922) foi um matemático russo.
                        Markov formou-se na Universidade Estatal de São Petersburgo em 1878, onde foi professor em 1886.

                        Em matemática, uma cadeia de Markov é um caso particular de processo estocástico com estados
                        discretos (o parâmetro, em geral o tempo, pode ser discreto ou contínuo) com a propriedade de que a distribuição de
                        probabilidade do próximo estado depende apenas do estado atual e não na sequência de eventos que precederam, uma propriedade
                        chamada de Markoviana, chamada assim em homenagem ao matemático.
                        A definição dessa propriedade, também chamada de memória markoviana, é que os estados anteriores são irrelevantes para a predição
                        dos estados seguintes, desde que o estado atual seja conhecido. Cadeias de Markov têm muitas aplicações como modelos estatísticos
                        de processos do mundo real.
                    </span>
                    <img src={andreiMarkov} alt="andrei-markov" />
                </main>
            </div>
        </>
    )
}

export default CadeiMarkov