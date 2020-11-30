import React, { CSSProperties, useState, useEffect, ChangeEvent, FormEvent } from 'react'
import Checkbox from '../Checkbox/index'
import andreiMarkov from '../../images/andrei_markov.svg'
import './style.css'


interface Style {
  style: CSSProperties
}

function Menu(props: Style) {
  const [search, setSearch] = useState<string>('')
  const [publicTweetsCheckbox, setPublicTweetsCheckbox] = useState<boolean>(false)
  const [timelineCheckbox, setTimelineCheckbox] = useState<boolean>(false)

 
  function handleCheckbox(event: ChangeEvent<HTMLInputElement>) {
    const { value }  = event.target

    if (value === 'Timeline') {
      setTimelineCheckbox(!timelineCheckbox)
      setPublicTweetsCheckbox(false)
    } 
    else if (value === 'Tweets públicos') {
      setPublicTweetsCheckbox(!publicTweetsCheckbox)
      setTimelineCheckbox(false)
    }
  }

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
      e.preventDefault()
      console.log(search)
      setSearch("")
  }

  useEffect(() => {
    setPublicTweetsCheckbox(false)
    setTimelineCheckbox(false)
    setSearch('')
  }, [props])

  return (
    <>
      <div id='flyoutMenu' style={props.style}>
        <form onSubmit={handleSubmit}>
          <div className="search">
            <label htmlFor="search">Informe sobre qual assunto, pessoa ou timeline deseja gerar texto.</label>
            <input
              value={search}
              onChange={(e: ChangeEvent<HTMLInputElement>) => setSearch(e.target.value)}
              type="text"
              name="search"
              placeholder="Ex: @pessoa, #tag ou nick"
              id="search"
            />
          </div>
          <div className="checkbox">
            <Checkbox value="Timeline" checked={timelineCheckbox} onChange={handleCheckbox} />
            <Checkbox value="Tweets públicos" checked={publicTweetsCheckbox} onChange={handleCheckbox} />
          </div>
          <button type="submit">iniciar</button>
        </form>
        <img src={andreiMarkov} alt="andrei-markov" width="696px" height="650" />
      </div>
    </>
  )
}

export default Menu