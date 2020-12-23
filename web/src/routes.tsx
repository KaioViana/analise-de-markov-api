import React from 'react'
import { BrowserRouter, Route } from 'react-router-dom'
import Landing from './pages/Landing/index'
import Desenvolvedor from './pages/Desenvolvedor/index'
import CadeiaMarkov from './pages/CadeiaMarkov/index'
import Result from './pages/Result/index'


function Routes() {
    return (
        <BrowserRouter>
            <Route path="/" exact component={Landing}/>
            <Route path="/desenvolvedor" exact component={Desenvolvedor}/>
            <Route path="/cadeia_markov" exact component={CadeiaMarkov}/>
            <Route path="/result" exact component={Result}/>
        </BrowserRouter>
    )
}

export default Routes