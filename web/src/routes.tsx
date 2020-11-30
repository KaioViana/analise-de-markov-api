import React from 'react'
import { BrowserRouter, Route } from 'react-router-dom'
import Landing from './pages/Landing/index'
import Desenvolvedor from './pages/Desenvolvedor/index'


function Routes() {
    return (
        <BrowserRouter>
            <Route path="/" exact component={Landing}/>
            <Route path="/desenvolvedor" exact component={Desenvolvedor}/>
        </BrowserRouter>
    )
}

export default Routes