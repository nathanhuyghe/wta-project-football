const axios = require('axios')
jest.mock('axios')


describe("mock api calls", () => {
    test("mocking endpoint team", () => {
        const mockedResponse = {"id":4,"name":"Manchester City","icon":"https://media.api-sports.io/football/teams/50.png","league":3}
        axios.get.mockResolvedValue(mockedResponse)
        const app = require('../app.js')
        app.getTeam()
        expect(axios.get).toHaveBeenCalled()
        expect(axios.get).toHaveBeenCalledWith('https://wta-project-football.azurewebsites.net/api/team/4/?format=json')
    })

    test("mocking endpoit league", () => {
        const mockedResponse = {"id":4,"name":"Jupiler Pro League","logo":"https://media.api-sports.io/football/leagues/144.png"}
        axios.get.mockResolvedValue(mockedResponse)
        const app = require('../app.js')
        app.getLeague()
        expect(axios.get).toHaveBeenCalled()
        expect(axios.get).toHaveBeenCalledWith('https://wta-project-football.azurewebsites.net/api/league/4/?format=json')

    })

    test("mocking endpoit lineup", () => {
        const mockedResponse = [{"id":345,"formation":"4-3-3","played":19,"team":4},{"id":346,"formation":"4-2-3-1","played":3,"team":4}]
        axios.get.mockResolvedValue(mockedResponse)
        
        const app = require('../app.js')
        app.getLineUps()
        expect(axios.get).toHaveBeenCalled()
        expect(axios.get).toHaveBeenCalledWith('https://wta-project-football.azurewebsites.net/api/lineups/4/?format=json')
    })
})