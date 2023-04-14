axios.get('http://127.0.0.1:3000/getall')
    .then(function (response) {
			console.log(response.data[0]);})
    .catch(function (error) {
      console.log(error);
    });