import './App.css';

function App() {
  return (
    <div className='d-flex align-items-center'>
    <div className="container content mt-3">
      <div className="p-5 text-center bg-body-tertiary rounded-3">
        {/* <svg className="bi mt-4 mb-3" style={{color: 'var(--bs-indigo)'}} width="100" height="100"></svg> */}
        <i class="bi bi-spotify text-success" style={{ 'font-size': '5em'}}></i>
        <h1 className="text-body-emphasis">Cluster your Spotify Playlist</h1>
        <p className="col-lg-8 mx-auto fs-5 text-muted">
          Use our first Spotify Playlist
        </p>
        <div className="d-inline-flex gap-2 mb-5">
          <button className="d-inline-flex align-items-center btn btn-dark btn-lg px-4 rounded-pill" type="button">
            Start
            <i class="ms-2 bi bi-box-arrow-in-right"></i>
         </button>
        </div>
      </div>
    </div>
    </div>
  );
}

export default App;
