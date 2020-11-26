import React, { CSSProperties, useState, ChangeEvent, useEffect } from 'react'
import andreiMarkov from '../../images/andrei_markov.svg'
import './style.css'


interface Style {
    style: CSSProperties
}

interface Checkbox {
    id: number,
    value: string,
    isChecked: boolean
}

function Menu(props: Style) {
    const [checkboxes, setcheckboxes] = useState<Checkbox[]>([
        {id: 1, value: "Tweets públicos", isChecked: false},
        {id: 2, value: "Timeline", isChecked: false}
    ])

    function handleCheckbox(event: ChangeEvent<HTMLInputElement>) {  
        console.log(event.target.value) 

        let checkboxesState = checkboxes

        checkboxesState.forEach(checkbox => {
            if (checkbox.value === event.target.value) {
                checkbox.isChecked = event.target.checked
            } else {
                checkbox.isChecked = false
            }
        })
        setcheckboxes(checkboxesState)
        console.log(checkboxes)
    }

    return (
        <div id='flyoutMenu' style={props.style}>
            <div className="search">
                <label htmlFor="search">Informe sobre qual assunto, pessoa ou timeline deseja gerar texto.</label>
                <input 
                    type="text"
                    name="search"
                    placeholder="Ex: @pessoa, #tag ou nick"
                    id="search"
                />
            </div>
            <div className="checkbox">
                {
                    checkboxes.map((checkbox: Checkbox) => {
                        return (
                            <>
                            <span className="custom-checkbox">
                                <input type="checkbox"  value={checkbox.value} onChange={handleCheckbox}/>
                                <span className="checked"></span>
                            </span>
                            <span className="text">{checkbox.value}</span>
                            </>
                        )
                    })
                }
                <button>iniciar</button>
            </div>
            <img src={andreiMarkov} alt="andrei-markov" width="696px" height="650"/>
        </div>
    )
}

export default Menu