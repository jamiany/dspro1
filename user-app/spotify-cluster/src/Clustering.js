import { useState, useEffect } from 'react';
import { useParams } from 'react-router';

export default function Clustering() {
    const params = useParams();

    const [detail, setDetail] = useState(null)

    const fetchInfo = () => { 
        return fetch('http://127.0.0.1:8000/api/startclustering/' + params.id, { method: 'POST' }) 
                .then((res) => res.json()) 
                .then((d) => {
                    setDetail(d)
                }) 
    }
        
    useEffect(() => {
        fetchInfo();
    }, [])

    return (
        <>
            <h1 className="display-1 text-center">Clustering</h1>
            <p className="text-center text-muted">Starting Clustering {detail && detail.name}</p>
        </>
    )
}