


const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
const data = {
  labels: labels,
  datasets: [{
    label: 'My First Dataset',
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    backgroundColor: 'rgba(248, 248, 244, 0.1)',
    tension: 0.1
  }]
};

// Config
const config = {
  type: 'line',
  data: data,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Monthly Data Line Chart'
      }
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
};

// Render the chart
const myChart = new Chart(
  document.getElementById('myChart'),
  config
);