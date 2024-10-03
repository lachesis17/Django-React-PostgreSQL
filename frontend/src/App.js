import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';
import './App.css';

function App() {
  const return_results = useState(null);

  const [fade_header, setFadeInHeader] = useState(false); // states for rendering with a fade animation
  const [fade_text, setFadeInTextInput] = useState(false);
  const [fade_img, setFadeInImage] = useState(false);

  useEffect(() => { // stagger the fades - unmountOnExit prop is needed in the transition to prevent initial rendering
    setTimeout(() => {setFadeInHeader(true);}, 625);
    setTimeout(() => {setFadeInTextInput(true);}, 1250);
    setTimeout(() => {setFadeInImage(true);}, 1875);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <CSSTransition in={fade_header} timeout={1250} classNames="fade" unmountOnExit>
          <h1 className="Headers">Such homepage, many wow.</h1></CSSTransition>
        <CSSTransition in={fade_img} timeout={1250} classNames="fade" unmountOnExit>
          <a href="https://github.com/lachesis17/" className="git-link"><img id="git" src="gitLogo.png" alt="" width="200px" height="200px" /></a></CSSTransition>
      </header>
    </div>
  );
}

export default App;