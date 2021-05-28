var country = ["SELECT", "US", "Spain", "Italy", "France", "Canada", "Argentina", "Australia"]
console.log(country) 
  var cosamples = country;
  console.log(cosamples)

function init() {
var gcountry = cosamples[1]
var idb1 = ["../static/scripts/dwreadall.json"]
  console.log(idb1)
  d3.json(idb1).then((d) => {
    var samples=d;
    console.log(samples)
    console.log(samples.deslen)
    console.log(samples.price_range)
    console.log(samples.variety)
    console.log(samples.province)

    var samplesdeslen = samples.deslen;   
    var samplesprice = samples.price_range;
    var samplesvariety = samples.variety;
    var samplesprovince = samples.province;
  })};

d3.select("selDataset_deslen").html(""); 
d3.select("selDataset_pricerange").html("");
d3.select("selDataset_variety").html("");
d3.select("selDataset_province").html("");
var countryget = document.getElementById("selDataset_country");
for (var i = 0; i<country.length; i++) {
  var opt = country[i];
  var el = document.createElement("option");
  el.textContent = opt;
  el.value = opt;
  countryget.appendChild(el);
  console.log(el, opt)
}
console.log(countryget)

document.getElementById("selDataset_country").onchange = function(){getData()};
function getData(){
  var gcountry = document.getElementById("selDataset_country").value; 
  console.log(document.getElementById("selDataset_country").value)
  console.log(gcountry)

  if (document.getElementById("selDataset_country").value == country[1]){idb1 = ["../static/scripts/dwreadall.json"];}
  else if (document.getElementById("selDataset_country").value == country[2]){idb1 = ["../static/scripts/dwreadspa.json"];}
  else if (document.getElementById("selDataset_country").value == country[3]){idb1 = ["../static/scripts/dwreadita.json"];}
  else if (document.getElementById("selDataset_country").value == country[4]){idb1 = ["../static/scripts/dwreadfra.json"];}
  else if (document.getElementById("selDataset_country").value == country[5]){idb1 = ["../static/scripts/dwreadcan.json"];}
  else if (document.getElementById("selDataset_country").value == country[6]){idb1 = ["../static/scripts/dwreadarg.json"];}
  else if (document.getElementById("selDataset_country").value == country[7]){idb1 = ["../static/scripts/dwreadaus.json"];}
  else {idb1 = ["../static/scripts/dwreadall.json"];}
  console.log(idb1)
 
  d3.json(idb1).then((d) => {
    var samples=d;
    console.log(samples)
    console.log(samples.deslen)
    console.log(samples.price_range)
    console.log(samples.variety)
    console.log(samples.province)

    var samplesdeslen = samples.deslen;   
    var samplesprice = samples.price_range;
    var samplesvariety = samples.variety;
    var samplesprovince = samples.province;

    var deslen = document.getElementById("selDataset_deslen");
    for (var i = 0; i<samplesdeslen.length; i++) {
      var opt = samplesdeslen[i];
      var el = document.createElement("option");
      el.textContent = opt;
      el.value = opt;
      deslen.appendChild(el);
      console.log(el, opt)
    }    
    var price_range = document.getElementById("selDataset_pricerange");
    for (var i = 0; i<samplesprice.length; i++) {
      var opt = samplesprice[i];
      var el = document.createElement("option");
      el.textContent = opt;
      el.value = opt;
      price_range.appendChild(el);
    }
    var variety = document.getElementById("selDataset_variety");
    for (var i = 0; i<samplesvariety.length; i++) {
      var opt = samplesvariety[i];
      var el = document.createElement("option");
      el.textContent = opt;
      el.value = opt;
      variety.appendChild(el);
    }
    var province = document.getElementById("selDataset_province");
    for (var i = 0; i<samplesprovince.length; i++) {
      var opt = samplesprovince[i];
      var el = document.createElement("option");
      el.textContent = opt;
      el.value = opt;
      province.appendChild(el);
    }

    document.getElementById("selDataset_deslen").onchange = function(){getData()};
    function getData(){
    var gdeslen = document.getElementById("selDataset_deslen").value;
    console.log(gdeslen)  
    }
    document.getElementById("selDataset_pricerange").onchange = function(){getData()};
    function getData(){
    var gprice_range = document.getElementById("selDataset_pricerange").value;
    console.log(gprice_range)
    }  
    document.getElementById("selDataset_variety").onchange = function(){getData()};
    function getData(){
    var gvariety = document.getElementById("selDataset_variety").value;
    console.log(gvariety)
    }
    document.getElementById("selDataset_province").onchange = function(){getData()};
    function getData(){
    var gprovince = document.getElementById("selDataset_province").value;
    console.log(gprovince)
    }
    init();
})};

