import React from 'react'
import Cloud from 'react-d3-cloud'
import stopword from 'stopword'
import './style.css'


interface CorpusWords {
    corpusWords: string[]
}

interface DataType {
    text: string
    value: number
}

function WordCloud(props: CorpusWords) {
    const fontSizeMapper = word => Math.log2(word.value) * 6
    const rotate = word => word.value % 360
    const especialsCharacters = [
        '.', 
        ',',
        ';',
        '=',
        '+',
        '"',
        '/',
        '*',
        ':',
        '!',
        "'",
        '-',
        '?'
    ]
    const corpusWords = stopword.removeStopwords(props.corpusWords, [...stopword.ptbr, ...especialsCharacters])

    let wordData: DataType[] = []

    corpusWords.forEach(word => {
        let index = wordData.findIndex(obj => obj.text === word)

        if (index < 0) {
            wordData.push({text: word, value: 1})
        } else {
            wordData[index].value += 1
        }
    })

    wordData.sort((a:DataType, b:DataType) => {
        return (a.value > b.value) ? -1 : ((b.value > a.value) ? 1 : 0)
    })

    wordData = wordData.slice(0, 250)
    
    return (
        <>
            <div className="word-cloud">
                <Cloud
                    data={wordData}
                    fontSizeMapper={fontSizeMapper}
                    rotate={rotate}
                    width={700}
                    height={400}
                />
            </div>
        </>
    )
}

export default WordCloud