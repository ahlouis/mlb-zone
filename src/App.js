import mlbLogo from './mlbLogo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={mlbLogo} className="App-logo" alt="logo" />
        <h1>MLB Zone</h1>
        <p>
          Hub for everything baseball, from fantasy to predictions.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
        </a>
      </header>
    </div>
  );
}

export default App;
