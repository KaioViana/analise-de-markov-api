import React, { useState, useEffect } from 'react'
import Load from '../../components/Load/index'
import WordCloud from '../../components/WordCloud/index'
import { Link } from 'react-router-dom'
import { AxiosResponse } from 'axios'
import api from '../../services/api'
import './style.css'


function Result() {
    const [load, setLoad] = useState<boolean>(true)
    const [text, setText] = useState<string>('')
    const [corpusWords, setCorpusWords] = useState<string[]>([])
    const [distinctWords, setDistinctWords] = useState<string[]>([])

    const loadedOrNot = () => {
        return load ? { heigth: '100vw' } : { marginTop: '-1000px' }
    }

    const clearLocalStorage = () => {
        localStorage.clear()
    }

    useEffect(() => {
        const data = {
            search: localStorage.getItem('search'),
            category: localStorage.getItem('category')
        }

        async function relatedSearch() {
            const response: AxiosResponse = await api.post('related-search', data)
            console.log(response.data)
            setText(response.data.text)
            setCorpusWords(response.data.corpus_words)
            setDistinctWords(response.data.distinct_words)
            setLoad(false)
        }

        relatedSearch()

    }, [])


    return (
        <div id="result-page">
            <div className="load">
                <Load style={loadedOrNot()} />
            </div>
            <header>
                <Link to="/" onClick={clearLocalStorage}>
                    Início
                </Link>
            </header>
            <div className="dados">
                <span className="entrada">
                    Entrada:
                    <span><br/>search: {localStorage.getItem('search')}<br/>category: {localStorage.getItem('category')}</span>
                </span>
                <strong className="nuvem">
                    Nuvem de Palavras
                    <span></span>
                </strong>
                <span className="tokens">
                    Tokens:
                    <span><br/>distintos: {distinctWords.length}<br/>total: {corpusWords.length}</span>
                </span>
            </div>
            <div className="cloud">
                <WordCloud
                    corpusWords={corpusWords}
                />
            </div>
            <div className="texto">
                <strong>TEXTO GERADO:</strong>
            </div>
            <span className="texto-gerado">
                {text}
            </span>
        </div>
    )
}

export default Result