async function draw() {
  // data
  const dataset = await d3.json('data.json')

  const xAccessor = (d) => d.currently.humidity
  const yAccessor = (d) => d.currently.apparentTemperature
}


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

// container width
dimensions.ctrWidth = dimensions.width - dimensions.margin.left - dimensions.margin.right

// container height
dimensions.ctrHeight = dimensions.height - dimensions.margin.top - dimensions.margin.bottom

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

// Adding a scale
const xScale = d3.scaleLinear()
  .domain(d3.extent(dataset, xAccessor))
  .range([0, dimensions.ctrWidth])

const yScale = d3.scaleLinear()
  .domain(d3.extent(dataset, yAccessor))
  .range([0, dimensions.ctrHeight])

// draw circles
ctr.selectAll('circle')
  .data(dataset)
  .join('circle')
  //.attr('cx', (d) => console.log(d))
  .attr('cx', d => xScale(xAccessor(d)))
  .attr('cy', d => yScale(yAccessor(d)))
  .attr('r', 5)
  .attr('fill', 'red')



// calling above function
draw()