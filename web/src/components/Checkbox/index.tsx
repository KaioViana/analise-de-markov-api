import React from 'react'
import './style.css'


interface CheckboxType {
    value: string
    checked: boolean
    onChange: any
}

function Checkbox(props: CheckboxType) {

    return (
        <div className="checkbox">
            <span className="text">
                <span className="custom-checkbox">
                    <input 
                        type="checkbox" 
                        value={props.value} 
                        checked={props.checked} 
                        onChange={props.onChange}
                    />
                    <span className="checked"/>
                </span>
                {props.value}
                </span>    
        </div>
    )

}

export default Checkbox