<script lang="ts">
  import { push, pop, replace } from "svelte-spa-router";
  import { st_standing, leagues_store, st_standings, st_teams, st_team } from "../store.js";
  import GetLeagues from "../requests/GetLeagues.svelte";

  let leagues = [];
  let teams = [];
  let standings = [];

  leagues_store.subscribe((value) => {
      leagues = value;
  })

  type League = {
    id: number,
    name: string,
    logo: string
  }

  type Standing = {
    id: number,
    points: number,
    form: string,
    rank: number,
    played: number,
    win: number,
    draw: number,
    loss: number,
    league: number,
    team: number
  }

  const go_league = (league: League) => () => {    
      standings.splice(0, standings.length);

      fetch("https://wta-project-football.azurewebsites.net/api/standings/"+ league.id + "/?format=json")
          .then(response => response.json()) 
          .then(data => {
              st_standings.set(data);
              standings = data;
              get_teams();
          }).catch(error => {
              console.log(error);
              return [];
      });
  };

  function get_teams() {
    teams.splice(0,teams.length);

    standings.forEach(obj => {
      fetch("https://wta-project-football.azurewebsites.net/api/team/"+ obj.team + "/?format=json")
        .then(response => response.json()) 
        .then(data => {
            teams.push(data);
            st_teams.set(teams);
        }).catch(error => {
            console.log(error);
            return [];
      });
    })  
    st_teams.subscribe((value) => {
      teams = value;
    })
  }

  const go_team = (stand: Standing) => () => {
    fetch("https://wta-project-football.azurewebsites.net/api/team/"+ stand.team + "/?format=json")
        .then(response => response.json()) 
        .then(data => {
            st_team.set(data);
            do_push(stand);
        }).catch(error => {
            console.log(error);
            return [];
      });
  };

  function do_push(stand) {
    st_standing.set(stand);
    push("/team/" + stand.team);
  }

</script>

<style lang="scss">
  $color-white: #eef5f7;
  $color-lightblue: #2E9CCA;
  $text-size: 1.2em;

    h2 {
      color: $color-white;
    }
    
    #container  {
      width: 65%;
      margin: auto auto;
      margin-top: 5rem;

      h1 {
        text-align: center;
        color: $color-white;
      }

      .btn-group button {
        background-color: $color-white;
        border: 1px solid $color-white;
        color: black;
        cursor: pointer;
        width: 100%;
        display: block;
        text-align: left;
      }

      button {
        height:4em;
        display: flex;
        flex-direction: row;
        font-size: $text-size;
        border-radius: 0.5em;
      }

      .btn-group button:hover {
        background-color: $color-lightblue;
      }

      button:focus {
        background-color: $color-lightblue;
      }

      .leagues {
        float: left;
      }

      .leaderboard {
        float: right;
      }

      img {
        max-height: 3em;
        width: 20%;
        vertical-align: middle;
        margin-right: 1em;
        margin-left: 1em;
      }
        
      table {
        margin-bottom: 3em;
        border-collapse: collapse;
        cursor: pointer;
        font-size: $text-size;

        td, th {
          border: 1px solid $color-white;
          padding: 0.5rem;
          text-align: left;
          color: $color-white;
        }
          
        tr:hover {
          background: $color-lightblue;
        }
      }  
    }

  </style>


<GetLeagues />
<div id="container">
  <h1>This is football!</h1>
  <div class="btn-group leagues">
    <h2>Leagues:</h2>
    {#each leagues as league}
      <button on:click={go_league(league)}>
        <img
          src={league.logo}
          alt="This is the logo of {league.name}"
        />
        <span class="logotext">{league.name}</span>
      </button>
    {/each}
  </div>

  <div class="btn-group leaderboard">
    <h2>Leaderboard:</h2>
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Team</th>
          <th>Points</th>
        </tr>
      </thead>
      <tbody>
        {#each standings as standing}
          <tr on:click={go_team(standing)}>
            <td>{standing.rank}</td>
            {#each teams as team }
              {#if team.id == standing.team}                   
                <td><img src={team.icon} alt="This is the logo of {team.name}"/> {team.name}</td>    
              {/if}
            {/each}
            <td>{standing.points}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>