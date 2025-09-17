import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  /*const [count, setCount] = useState(0)*/
  const [description, setDescription] = useState('')
  const [serverResponse, setServerResponse] = useState('')
  const [classification, setClassification] = useState<any>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)
  async function submitDescription(text: string) {
    try {
      setIsSubmitting(true);
      const res = await fetch('http://localhost:8001/api/process-project', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description: text }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setServerResponse(data.status === 'success' ? 'Project processed successfully!' : data.message);
      setClassification(data.classification || null);
      console.log('API response:', data);
      return data;
    } catch (err) {
      console.error('Request failed:', err);
      throw err;
    }
    finally{
      setIsSubmitting(false);
    }
  }
  async function submitFile(file: File) {
    const form = new FormData();
    try {
      form.append('file', file)
      setIsSubmitting(true);
      const res = await fetch('http://localhost:8001/api/process-project-file', {
        method: 'POST',
        body: form,
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      console.log('File upload response:', data)
      return data;
    } catch (err) {
      console.error('Request failed:', err);
      throw err;
    }
    finally{
      setIsSubmitting(false);
    }
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      {/*<h1>Vite + React</h1>*/}
      <h1>Business Impact Simulator</h1>
      <div className="card">
        <input type="text"
         placeholder = "Enter your project description or upload a file "
         style={{ padding: '10px', width: '300px' }}
         value = {description}
         onChange={(e) => setDescription(e.target.value)}/>
        <input 
          type = "file"
          accept = ".txt, .pdf,.json"
          style = {{padding: '10px'}} 
          onChange={(e) => {
            const file = (e.target as HTMLInputElement).files?.[0];
            if (file) submitFile(file);
          }}/>
        <button type = "button" disabled= {isSubmitting} aria-busy={isSubmitting} onClick={() => submitDescription(description)}
               >{isSubmitting ? 'Sending…' : 'Submit to backend'}</button>
        {serverResponse && <p>Server said: {serverResponse}</p>}
        
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
