jQuery(function($){
	// Charts js code
	var weekly_trends_chart = function(){
		config = {
		    type: 'bar',
		    data: {
		        labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
		        datasets: [{
		            label: "Queue Numbers",
		            data: [140, 79, 120, 172, 58],
		            backgroundColor: 'rgba(0, 188, 212, 0.8)'
		        }]
		    },
		    options: {
		        responsive: true,
		        legend: false
		    }
		}
		return config;
	};

    new Chart(document.getElementById("weekly-trends-chart").getContext("2d"), weekly_trends_chart());
});