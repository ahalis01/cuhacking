import React from 'react';
import Particles from 'react-particles-js';
import './App.css';

const particlesConfig ={
	    "particles": {
	        "number": {
	            "value": 50
	        },
	        "size": {
	            "value": 3
	        }
	    },
	    "interactivity": {
	        "events": {
	            "onhover": {
	                "enable": true,
	                "mode": "repulse"
	            }
	        }
	    }
	}
class MyForm extends React.Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const data = new FormData(form);
    
    fetch('www.google.com', {
      method: 'POST',
      body: data,
    });
  }

  render() {
    return (
	<div className="App">
	    Twitter Bot Detector
	<div className="App-header">
	    
      <form onSubmit={this.handleSubmit}>
        <input name="username" type="text"/>
        <button>Check profile!</button>
      </form>
	</div>	
	</div>
    );
  }
}

export default MyForm;


