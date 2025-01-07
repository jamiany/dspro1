import { useState, useEffect } from 'react';
import { useParams } from 'react-router';

export default function Clustering() {
    const params = useParams();

    const [detail, setDetail] = useState(null)

    const fetchInfo = () => { 
        return fetch(`http://127.0.0.1:8000/api/startclustering/${params.id}/${params.clusters}`, { method: 'POST' }) 
                .then((res) => res.json()) 
                .then((d) => {
                    setDetail(d);
                })
    }
        
    useEffect(() => {
        fetchInfo()
            .then(_ => {
            });
            console.log(detail)
        }, []);

    return (
        <>
            <h1 className="display-1 text-center">Clustering</h1>
            <p className="text-center text-muted">Starting Clustering</p>
            <div className='row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4'>
                {detail && Object.entries(detail).map(x => 
                    <div className='col'>
                        <div className="card">
                        <div className="card-header">
                        #{+x[0] + 1}
                        </div>
                        <ul className="list-group list-group-flush">
                            {detail[x[0]].map(y => <a target='_blank' href={'https://open.spotify.com/track/' + y.id}><li className="list-group-item">{y.name} - {y.artist}</li></a>)}
                        </ul>
                    </div>
                </div>
                )}
            </div>
        </>
    )
}