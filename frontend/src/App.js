import React, { useState, useEffect } from 'react';
import { CSSTransition } from 'react-transition-group';
import './App.css';
import { useQuery, gql } from '@apollo/client';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const GET_QC_FS = gql`
  {
    allCptData {
      depth
      qc
      fs
    }
  }
`;

const GET_U = gql`
  {
    allCptData {
      depth
      u
    }
  }
`;

function QcFsChart() {
  const { loading, error, data } = useQuery(GET_QC_FS);

  if (loading) return <p>Loading chart data...</p>;
  if (error) return <p>Error loading chart data: {error.message}</p>;

  return (
    <LineChart 
      width={700} 
      height={500} 
      layout="vertical" 
      data={data.allCptData}
      margin={{ top: 5, right: 0, bottom: 10, left: 100 }}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis type="number" tick={{ fontSize: '14px' }} />
      <YAxis dataKey="depth" type="number" tick={{ fontSize: '14px' }} />
      <Tooltip />
      <Legend wrapperStyle={{ marginLeft: 30 }}/>
      <Line type="monotone" dataKey="qc" stroke="#8884d8" dot={{ r: 2, fill: '#8884d8', stroke: '#ffffff', strokeWidth: 0.66 }} />
      <Line type="monotone" dataKey="fs" stroke="#82ca9d" dot={{ r: 2, fill: '#82ca9d', stroke: '#ffffff', strokeWidth: 0.66 }} />
    </LineChart>
  );
}

function UChart() {
  const { loading, error, data } = useQuery(GET_U);

  if (loading) return <p>Loading chart data...</p>;
  if (error) return <p>Error loading chart data: {error.message}</p>;

  return (
    <LineChart 
      width={700} 
      height={500} 
      layout="vertical" 
      data={data.allCptData}
      margin={{ top: 5, right: 0, bottom: 10, left: 100 }}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis type="number" tick={{ fontSize: '14px' }} />
      <YAxis dataKey="depth" type="number" tick={{ fontSize: '14px' }} />
      <Tooltip />
      <Legend wrapperStyle={{ marginLeft: 30 }}/>
      <Line type="monotone" dataKey="u" stroke="#ca8282" dot={{ r: 2, fill: '#ca8282', stroke: '#ffffff', strokeWidth: 0.66 }} />
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
          <h1 className="Headers">Such homepage, many wow. <img id="doge" src="static/build/doge.png" alt="" width="42px" height="42px" /></h1></CSSTransition>
        <CSSTransition in={fade_chart} timeout={1250} classNames="fade" unmountOnExit>
          <div className="chart-container">
            <QcFsChart /><UChart />
            </div></CSSTransition>
        <CSSTransition in={fade_img} timeout={1250} classNames="fade" unmountOnExit>
          <a href="https://github.com/lachesis17/" className="git-link"><img id="git" src="static/build/gitLogo.png" alt="" width="200px" height="200px" /></a></CSSTransition>
      </header>
    </div>
  );
}

export default App;