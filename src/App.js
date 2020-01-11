import React from 'react';
import Slider from '@material-ui/core/Slider';
import floorPlan from './1.svg'
import './App.css';

function App() {
  return (
    <div className="App">
	<div className="TimeSelector">
	   <Slider
		aria-labelledby="discrete-slider-always"
        	valueLabelDisplay="on"
	   ></Slider>
	</div>
      <header className="App-header">
        <img src={floorPlan} className="floorplan" alt="logo" />
      </header>
    </div>
  );
}

export default App;
