$(document).ready(function(){
 var _data = [];
 var _labels = [];

 var chart = new Chart(document.getElementById("myChart"), {
   
  type: 'line',
  data: {
    labels: _labels,
    datasets: [
    {
      label: "Sentiment (-1 to 1)",
      backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
      data: _data
      }
      ]
      },
        options: {
        legend: { display: false },
          title: {
          display: true,
          text: 'Sentiment'
    }
    }
 });

 var dps = [];
 var xVal = 0;
 var yVal = 0; 
 var updateInterval = 1000;
 var dataLength = 20; // number of dataPoints visible at any point
 
 var updateChart = function (count) {
 
 	count = count || 1;
  $.ajax({
      type: "GET",
      url: "/get_data",
      data: {vals: ''},
      success: function(response) {
        full_data = JSON.parse(response.payload);
        yVal = full_data["data"];
      },
    
     });
   
  xVal++;
  chart.data.datasets[0].data.push(yVal)
  //window.alert(chart.data.datasets[0].data)
  chart.data.labels.push(xVal)

 	if (chart.data.datasets[0].data.length > dataLength) {
    chart.data.datasets[0].data.shift();
    chart.data.labels.shift();
   }
  
  
 	chart.update();
 };
 
 updateChart(dataLength);
 setInterval(function(){updateChart()}, updateInterval);

});