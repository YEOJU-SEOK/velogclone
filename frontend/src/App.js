import React from 'react';
import './App.css';
import Navi from './components/Navi';
import Header from './components/Header';
import LoginModal from './components/LoginModal';
import { Route } from 'react-router-dom';

function App() {

  return (
    <>
      <div className="App">
        <div className="auto-margin">
        
          <Route exact path="/">
            <Header modal={modal}/>
          </Route>

          <Route exact path="/">
            <Navi/>
          </Route>

          <Route exact path="/login">
            <LoginModal setModal={setModal}/>
          </Route>
          
      </div>
    </div>
    </>
  );
}

export default App;