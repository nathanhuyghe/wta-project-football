const axios = require('axios')

function getTeam(){
    axios.get('https://wta-project-football.azurewebsites.net/api/team/4/?format=json')
    .then(response => console.log(response))
    .catch(error => console.log(error))
}

function getLeague(){
    axios.get('https://wta-project-football.azurewebsites.net/api/league/4/?format=json')
    .then(response => console.log(response))
    .catch(error => console.log(error))
}

function getLineUps(){
    axios.get('https://wta-project-football.azurewebsites.net/api/lineups/4/?format=json')
    .then(response => console.log(response))
    .catch(error => console.log(error))
}

module.exports = {getTeam, getLeague, getLineUps}

