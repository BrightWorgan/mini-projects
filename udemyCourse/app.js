// selection class
//const pBrowser = document.querySelector('p')
//const pD3 = d3.select('p')

//console.log(pBrowser)
//console.log(pD3)

// transformation class

// classes and styles class
//const el = d3.select('body')
//  .append('p')
//.attr('class', 'foo')
//.text('Hello Wordld')

// joining data class

//const el = d3.select('body')
//  .append('p')
//.classed('foo', true)
//  .classed('bar', true)
//  .text('Hello World Third Text Sample')
//  .style('color', 'blue')

const data = [10, 20, 30, 40, 50]
const el = d3.selectA('ul')
  .selectAll('li')
  .data(data)
  .join('li')
  .text('hello')
consoile.log(el)