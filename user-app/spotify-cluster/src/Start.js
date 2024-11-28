import { useState, useEffect } from "react"

export default function Start() {
    const [playlist, setPlaylist] = useState(null)

    const fetchInfo = () => { 
        return fetch('http://127.0.0.1:8000/api/playlist') 
                .then((res) => res.json()) 
                .then((d) => setPlaylist(d)) 
    }
        
    useEffect(() => {
        fetchInfo();
    }, [])

    return (
        <div>
            <p>{playlist && playlist.total}</p>
            <div>{playlist && playlist.items.map(i => <p>{i?.name}</p>)}</div>
        </div>
    )
}