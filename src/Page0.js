import React from 'react';
import MicIcon from '@mui/icons-material/Mic';
import MicOffIcon from '@mui/icons-material/MicOff';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';


const Page0 = ({ plainText, onPlainTextChange }) => {
    // Speech recognition 
    const {
      transcript,
      listening,
      resetTranscript,
      browserSupportsSpeechRecognition
    } = useSpeechRecognition();


    // Make sure browser supports speech recognition
    if (!browserSupportsSpeechRecognition) {
      return <span>Browser doesn't support speech recognition.</span>;
    }

    // Start/stop recording and update plaintext
    const toggleRecording = () => {
      if (listening) {
        SpeechRecognition.stopListening()
        onPlainTextChange(plainText + transcript)
      } else {
        SpeechRecognition.startListening({ continuous: true })
      }
      resetTranscript()
    }

    // Render page 0
    return (
        <div>
            <h1>Record Maintenance Routine</h1>
            <textarea id="text-form" value={listening ? transcript : plainText} onChange={(e) => onPlainTextChange(e.target.value)} disabled={listening}/>
            {listening ? <h3>Recording...</h3> : <h3>Press Microphone to Record</h3>}
            <div onClick={toggleRecording}>
                {listening ? <MicIcon id="input-mic" className="input-mic mic-on"/> : <MicOffIcon id="input-mic" className="input-mic mic-off"/>}
            </div>
      </div>
    )
}

export default Page0;