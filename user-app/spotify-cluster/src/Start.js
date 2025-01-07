import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom";

export default function Start() {
    const [playlist, setPlaylist] = useState(null);
    const [numberOfClusters, setNumberOfClusters] = useState(2);
    const navigate = useNavigate();

    const fetchInfo = () => { 
        return fetch('http://127.0.0.1:8000/api/playlist') 
                .then((res) => res.json()) 
                .then((d) => {
                    d.items = d.items.filter(x => x)
                    setPlaylist(d)
                }) 
    }
        
    useEffect(() => {
        fetchInfo();
    }, [])

    function startClutering() {
        let selectedPlaylist = document.getElementById('floatingSelect').value
        navigate(`/clustering/${selectedPlaylist}/${numberOfClusters}`);
    }

    return (
        <div>
            <h1 className="display-1 text-center">Select a playlist</h1>
            <p className="text-muted text-center">This playlist will be used to cluster the songs.</p>

            <div class="form-floating mt-3">
                <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
                    <option selected>--- select ---</option>
                    {playlist && playlist.items.map(i => <option value={i?.id}>{i?.name}</option>)}
                </select>
                <label for="floatingSelect">Playlist</label>
            </div>

            <div className="mt-3">
                <label for="customRange2" class="form-label">Number of clusters: {numberOfClusters}</label>
                <input type="range" class="form-range" min="2" max="10" id="range" value={numberOfClusters} onChange={e => setNumberOfClusters(e.target.value)}></input>
            </div>

            <div class="d-grid gap-2">
                <button onClick={startClutering} className="btn btn-dark mt-3">Start</button>
            </div>
        </div>
    )
}