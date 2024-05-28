import './App.css';
import React, { useState } from 'react';
import Navbar from './Navbar.js';
import Page0 from './Page0.js';
import Page1 from './Page1.js';
import ArrowCircleRightIcon from '@mui/icons-material/ArrowCircleRight';
import ArrowCircleLeftIcon from '@mui/icons-material/ArrowCircleLeft';

function App() {
  // Declare necessary variables
  const [clickedNext, setClickedNext] = useState(0);
  const [plainText, setPlainText] = useState('');

  // Function to update plaintext variable
  const handlePlainTextChange = (newPlainText) => {
    setPlainText(newPlainText);
  };

  // Dictionary to store all data
  const [data, setData] = useState({
    action_taken: "",
    malfunction_code: "",
    trans_code: -1,
    type_maf_code: "",
    type_maint_code: "",
    updown_ind: "",
    wc_code: "",
    wuc: -1
  });

  // Function to send post request to flask api
  const sendToFlaskApi = async (plainText) => {
    try {
      let request = {
        method: 'POST',
        mode: "cors",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(plainText),
      }

      console.log(request)
      const response = await fetch('http://127.0.0.1:8000/getTranscript', request);
  
      if (!response.ok) {
        throw new Error('Failed to send data to Flask API');
      }
  
      // Optionally handle the response from the Flask API
      const result = await response.json();
      console.log('Response from Flask API:', result);

      // Update data dictionary
      updateData(result);

    } catch (error) {
      console.error('Error sending data to Flask API:', error.message);
    }
  };

  // Take response from flask API, parse and update internal dictionary
  const updateData = (result) => {
    // Update the data dictionary
    setData({
      action_taken: result.action_taken[0],
      malfunction_code: result.malfunction_code[0],
      trans_code: result.trans_code[0],
      type_maf_code: result.type_maf_code[0],
      type_maint_code: result.type_maint_code[0],
      updown_ind: result.updown_ind[0],
      wc_code: result.wc_code[0],
      wuc: result.wuc[0],
    });
  }

  const nextPage = () => {
    // Update Page
    setClickedNext(clickedNext + 1);

    // Send data to backend
    sendToFlaskApi(plainText)
  }

  const prevPage = () => {
    // reset plaintext and data
    handlePlainTextChange("")
    setData({
      action_taken: "",
      malfunction_code: "",
      trans_code: -1,
      type_maf_code: "",
      type_maint_code: "",
      updown_ind: "",
      wc_code: "",
      wuc: -1
    })
    setClickedNext(clickedNext - 1);
  }

  // Upadate pages
  let page;
  if (clickedNext === 0) {
    page = <Page0 plainText={plainText} onPlainTextChange={handlePlainTextChange} />;
  } else if (clickedNext === 1 && data.action_taken) {
    page = <Page1 data={data} />;
  } 

  // Update pages
  let back;
  if (clickedNext === 1) {
    back = <div id="back-page" onClick={prevPage}>
            <ArrowCircleLeftIcon id="page-button"/>
            <p>Previous Step</p>
          </div>
  } else {
    back = "";
  }

  // Update pages
  let next;
  if (clickedNext === 0) {
    next = <div id="next-page" onClick={nextPage}>
            <ArrowCircleRightIcon id="page-button"/>
            <p>Next Step</p>
          </div>
  } else {
    next = "";
  }

  // Render app
  return (
    <div className="App">
      <Navbar />
      { page }
      { back }
      { next }
    </div>
  );
}

export default App;
