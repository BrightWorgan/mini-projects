async function draw() {
  // data
  const dataset = await d3.json('data.json')


  // dimension of scatter graph
  let dimensions = {
    width: 800,
    height: 800
  }

  // draw image
  const svg = d3.select('#chart')
    .append('svg')
    .attr('width', dimensions.width)
    .attr('height', dimensions.height)
}


// calling above function
draw()