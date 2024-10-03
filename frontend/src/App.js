import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';
import './App.css';
import { useQuery, gql } from '@apollo/client';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const GET_CPT_DATA = gql`
  {
    allCptData {
      depth
      qc
      fs
    }
  }
`;

function CptDataChart() {
  const { loading, error, data } = useQuery(GET_CPT_DATA);

  if (loading) return <p>Loading chart data...</p>;
  if (error) return <p>Error loading chart data: {error.message}</p>;

  return (
    <LineChart width={600} height={300} data={data.allCptData}
      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="depth" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="qc" stroke="#8884d8" activeDot={{ r: 8 }} />
      <Line type="monotone" dataKey="fs" stroke="#82ca9d" />
    </LineChart>
  );
}

function App() {
  const [fade_header, setFadeInHeader] = useState(false); // states for rendering with a fade animation
  const [fade_chart, setFadeInTextInput] = useState(false);
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
        <CSSTransition in={fade_chart} timeout={1250} classNames="fade" unmountOnExit>
          <CptDataChart /></CSSTransition>
        <CSSTransition in={fade_img} timeout={1250} classNames="fade" unmountOnExit>
          <a href="https://github.com/lachesis17/" className="git-link"><img id="git" src="gitLogo.png" alt="" width="200px" height="200px" /></a></CSSTransition>
      </header>
    </div>
  );
}

export default App;