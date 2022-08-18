function getData() {
  // getting data from JSON file
  //const data = await d3.json('data.json')
  // getting data from CSV file
  const data = await d3.csv('data.csv')

  console.log(data)
}

getData()