import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';

const App = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/data')
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    const chartData = {
        labels: data.map(d => d.timestamp),
        datasets: [{
            label: 'Headlines Count',
            data: data.map(d => d.count),
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true,
        }],
    };

    return (
        <div className="App">
            <h1>Crypto Data Viewer</h1>
            <Line data={chartData} />
        </div>
    );
};

export default App;
