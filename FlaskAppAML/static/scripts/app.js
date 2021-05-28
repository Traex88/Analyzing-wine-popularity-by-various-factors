var wineData

// Variable for XMLHttpRequest
var request = new XMLHttpRequest()


request.onload = function () {


  // Function for change on dropdown menu
function selectData(selectedCountry, runNum){

  // Check if value is selected in dropdown
  console.log(selectedCountry);
  

// Read the json file for the data
  d3.json("https://winery-api.azurewebsites.net/api/v1/resources/wines/all").then((data) => {
  
  wineData=data
  console.log(data);
  
  wineData.forEach(function(data) {
          data.price = +data.price;
          data.points = +data.points;
        });

  
  var uniqueCountries = [];


  for(i=0; i<data.length; i++){
    if(uniqueCountries.indexOf(data[i].country) === -1){
      uniqueCountries.push(data[i].country);
    }
  }

  console.log(uniqueCountries);
  // console.log(uniqueWineries);
  
  
  // Select the uniqueCountries array and for each item append the item ID and adds ID to dropdown
  if (runNum == 0){
    uniqueCountries.forEach(country =>
      {
 //       // console.log(item.id);

      d3.select("#selDataset").append('option').attr('value', country).text(country);
      });

  // Selected value is passed
  d3.select("#selDataset").node().value = selectedCountry;
  }

  var countryData = data.filter(winery=> (winery.country == selectedCountry));

  // Update the panel display to have the selected country
  var panelDisplay = d3.select("#sample-data");
  panelDisplay.html("");
  Object.entries(countryData[0]).forEach(winery=> 
     {
        console.log(winery);
        panelDisplay.append("p").text(`${winery[0]}: ${winery[1]}`)
     });

//   // BAR CHART

// Filter sample array data for the selected country
var countrySample = data.filter(winery => winery.country == selectedCountry);
  
// Check values
// console.log(countrySample);

  var wineryPoints = data.map(winery => winery.points)
  var winePrice = data.map(winery => winery.price)

  // Check values
  //  console.log(sampleValue);
  //  console.log(winePrice);
  //  console.log(wineryPoints);
  
  // Define the layout and trace object, edit color and orientation
  
  var trace1 = {
     y: wineryPoints,
     x: winePrice,
     type: 'bar',
     orientation: 'h',
     marker: {
       color: 'red',
       
     }
    },
  layout = {
     title: 'Price vs. Points by Country',
     xaxis: {title: 'Wine Valuation'},
     yaxis: {title: 'Points'}
     };

     var data1 = [trace1]

  // Plot using plotly  
  Plotly.plot("bar", data1, layout, {responsive: true});    

// // BUBBLE CHART

var countryArray = data.map(winery => winery.country)
// console.log(countryArray);

var countryCounts = {};
for (var i=0; i<countryArray.length; i++) {
  countryCounts[countryArray[i]] = 1 + (countryCounts[countryArray[i]] || 0);
}
// console.log(countryCounts);

var countryName = [];

var result = [];
for (var i in countryCounts) {
result.push(countryCounts[i]);
countryName.push(i);
}
// console.log(result)
// console.log(countryName);
// console.log(dataCounts);


var trace2 = {
  x: countryName,
  y: result,
  mode: 'markers',
  marker: {
    color: "red",

    size: result,
    sizeref: 500
  }
};

var data2 = [trace2];

var layout2 = {
  // title: 'Number of Wineries by Country',
  showlegend: false,
  height: 600,
  width: 600
};

// Plot using Plotly
Plotly.newPlot('bubble', data2, layout2);


var barTrace = {
  labels: ["US", "France", "Italy", "Spain",
   "Argentina", "Australia", "Canada",],
values: [50.0, 20.0, 17.9, 6.0, 3.0, 2.1, 1.1],
 type: 'pie'
};

var data = [barTrace];

var layoutTrace = {
 title: "Wineries per Country",
};

Plotly.newPlot("circle", data, layoutTrace);
  
  })

function optionChanged(winery) {
  console.log(winery);
  // resetData();
  selectData(winery, 1)
}

}
// Initial test starts at Italy
selectData("Italy", 0)

// Send request
request.send()