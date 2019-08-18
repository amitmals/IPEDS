
// Read the data set from MongoDB to create the drop down menu
function init() {
    console.log("Amit Malik-init()")
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");
    // Use the list of sample names to populate the select options
    d3.json("/coldata").then((sampleNames)=>{
        sampleNames.forEach((sample)=>{
            selector
                .append("option")
                .text(sample.name)
                .property("value",sample.name);
        });
    });
};


function updateJumbotron(univName){
    var PANEL = d3.select("#jumbotron-data");
    PANEL.html("");
    PANEL.append("h1").text(`${univName}`);
}



function optionChanged(newSample) {
    console.log(newSample);
    updateJumbotron(newSample);
    
}



// Initialize the dashboard for index.html
init();