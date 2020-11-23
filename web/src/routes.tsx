import React from 'react'
import { BrowserRouter, Route } from 'react-router-dom'
import Landing from './pages/Landing/index'


function Routes() {
    return (
        <BrowserRouter>
            <Route path="/" exact component={Landing}/>
        </BrowserRouter>
    )
}

export default Routes