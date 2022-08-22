async function draw() {
  // data
  const dataset = await d3.json('data.json')


  // dimension of scatter graph
  let dimensions = {
    width: 800,
    height: 800,
    margin: {
      top: 50,
      bottom: 50,
      left: 50,
      right: 50
    }
  }

  // draw image
  const svg = d3.select('#chart')
    .append('svg')
    .attr('width', dimensions.width)
    .attr('height', dimensions.height)

  const ctr = svg.append('g')
    .attr(
      'transform',
      `translate(${dimensions.margin.left}, ${dimensions.margin.top})`
    )

  // Commented out first test circle
  //ctr.append('circle')
  // .attr('r', 15)

  // draw circles
  ctr.selectAll('circle')
    .data(dataset)
    .join('circle')
    .attr('cx', () => )
}


// calling above function
draw()